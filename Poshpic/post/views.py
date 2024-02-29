from rest_framework.views import APIView
from .serializer import (
    PostSerializer,
    LikeSerializer,
    CommentSerializer,
    PostHistorySerializer,

)
from rest_framework.response import Response
from rest_framework import status
from .models import ( 
                Post,
                Like, 
                Comment, 
                PostHistory,
)
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from django.core.exceptions  import (
    ObjectDoesNotExist , 
    ValidationError,
)
from account.models import User
from .pagination import PostLimitOffsetPagination

class Post_PhototgrapherView(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = PostLimitOffsetPagination

    def get(self, request, format=None):
        
        try:
            posts = Post.objects.all().order_by('-created_at')
            paginator = self.pagination_class()
            result_page = paginator.paginate_queryset(posts, request)
            serializer = PostSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        except ObjectDoesNotExist:
            return Response({'msg':'No Posts found'} ,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
           return Response({'msg':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)   
       

    # def get(self, request, format=None):
    #     try:
    #         posts = Post.objects.all().order_by('-created_at')
    #         serializer = PostSerializer(posts, many=True)
    #         return Response(serializer.data)
    #     except ObjectDoesNotExist:
    #         return Response({'msg':'No Posts found'} ,status=status.HTTP_400_BAD_REQUEST)
    #     except Exception as e:
    #        return Response({'msg':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
    def post(self, request, *args, **kwargs):
        
        try:
            serializer = PostSerializer(data=request.data)
            user = request.user

            if serializer.is_valid():
                serializer.save(user=user, created_at=timezone.now())
                return Response(
                    {"msg": "post successfully created"},
                    status=status.HTTP_201_CREATED
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except ValidationError as e:
            return Response({'msg': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'msg': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def patch(self, request, pk, *args, **kwargs):
        try:
            post = Post.objects.get(pk=pk, user=request.user)
        except Post.DoesNotExist:
            return Response({"msg": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Post is updated"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, pk):
        try:
            post = Post.objects.get(pk=pk, user=request.user)
        except Post.DoesNotExist:
            return Response({'msg':'Not Found'}, status=status.HTTP_400_BAD_REQUEST )    

        try:
            PostHistory.objects.create(
                user=request.user,
                title=post.title,
                image=post.image,
            )
                
            post.delete()
            return Response({"msg": "post is deleted"}, status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return Response({"msg": "erorrr"}, status=status.HTTP_404_NOT_FOUND)
        
class Photographer_postApiview(APIView):
    def get(self, request):
        user = request.user
        try:
            posts = Post.objects.filter(user=user).prefetch_related('likes', 'comments').order_by('-created_at')
            if not posts.exists():
                return Response({'msg': 'No posts found for the user'}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = PostSerializer(posts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'msg': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        
class LikeApiView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        user = request.user
        try:
             post = Post.objects.get(id=pk)
        except Like.DoesNotExist:
            return Response({'msg':'Not found '} , status=status.HTTP_400_BAD_REQUEST )     

        existinglike = Like.objects.filter(user=user, post_id=pk).first()

        if existinglike:
            existinglike.delete()
            return Response({"msg": "unliked"}, status=status.HTTP_200_OK)
        else:
       
            user = user.id
            post = post.id

            serializer = LikeSerializer(data={"user": user, "post": post})
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "liked"}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk, *args, **kwargs):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({"msg": "post not fount"}, status=status.HTTP_404_NOT_FOUND)

        likes = post.posts.all()
        serializer = LikeSerializer(likes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
     

class PostHistoryListView(APIView):
    def get(self, request, pk=None, *args, **kwargs):
        user = request.user
        if pk is not None:
            try:
                posthistory = PostHistory.objects.get(id=pk , user= user)
                serializer = PostHistorySerializer(posthistory)
                return Response(serializer.data)
            except PostHistory.DoesNotExist:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = request.user
        posthistory = PostHistory.objects.filter(user=user)
        serializer = PostHistorySerializer(posthistory, many=True)
        return Response(serializer.data)

    # def delete(self, request, pk):
    #     try:
    #         post = PostHistory.objects.get(pk=pk, user=request.user)
    #     except PostHistory.DoesNotExist:
    #         return Response({'msg':"psot historry don't exixt"} , status=status.HTTP_400_BAD_REQUEST )
    #     try:
    #         post.delete()
    #         return Response({"msg": "post history deleted"}, status=status.HTTP_200_OK)
    #     except PostHistory.DoesNotExist:
    #         return Response(
    #             {"msg": "post history not found"}, status=status.HTTP_400_BAD_REQUEST
    #         )
            
    def delete(self, request, pk):
        try:
            post = PostHistory.objects.get(pk=pk, user=request.user)
            post.delete()
            return Response({"msg": "Post history deleted"}, status=status.HTTP_200_OK)
        except PostHistory.DoesNotExist:
            return Response({"msg": "Post history not found or you don't have permission"}, status=status.HTTP_404_NOT_FOUND)       


    def patch(self, request, pk, *args, **kwargs):
        try:
            post = PostHistory.objects.get(pk=pk, user=request.user)

        except PostHistory.DoesNotExist:
            return Response(
                {"msg": "post does not exist"}, status=status.HTTP_404_NOT_FOUND
            )
        try:
            serializer = PostHistorySerializer(post, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"msg": "server erorr"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class CommentApiView(APIView):
    permission_classes = {IsAuthenticated}

    def post(self, request, pk):
        post = Post.objects.get(id=pk)
        serializer = CommentSerializer(
            data={"post": post.id, "user": request.user.id, **request.data}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None, *args, **kwargs):
        try:

            post = Post.objects.get(id=pk)
          
            comments = Comment.objects.filter(post=post).order_by('-created_at')

            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return Response({"msg": "post not found"}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk, *args, **kwargs):
        try:
            comments = Comment.objects.get(id=pk, user=request.user)
        except Comment.DoesNotExist:
            return Response(
                {"msg": "comment not fount "}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = CommentSerializer(comments, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

      

    def delete(self, request, pk):

        try:
            comment = Comment.objects.get(id=pk, user=request.user)
            comment.delete()
            return Response({"msg": "Comment deleted"}, status=status.HTTP_200_OK)
        except Comment.DoesNotExist:
            return Response({"msg": "erorrr"}, status=status.HTTP_404_NOT_FOUND)


class RepostApiView(APIView):
    def post(self, request, pk, *args, **kwargs):
        try:
            post_history = PostHistory.objects.get(pk=pk, user=request.user)

            newdata = {
                "user": request.user.id,
                "image": post_history.image,
                "title": post_history.title,
                "description": post_history.description,
            }

            serializer = PostSerializer(data=newdata)
            if serializer.is_valid(raise_exception=True):
                print("iiiiiiiiii")
                serializer.save(user=request.user)

                post_history.delete()

                return Response(
                    {"msg": "Repost successful"}, status=status.HTTP_201_CREATED
                )

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except PostHistory.DoesNotExist:
            return Response(
                {"msg": "post histry not found"}, status=status.HTTP_404_NOT_FOUND
            )
            
            
            

            
                    

































  # def delete(self, request, pk, format=None):
        # comment = get_object_or_404(Comment, pk=pk)
        # if request.user != comment.user:
        #     return Response(
        #         {"error": "You do not have permission to delete this comment."},
        #         status=status.HTTP_403_FORBIDDEN,
        #     )
        # comment.delete()
        # return Response(
        #     {"message": "Comment deleted successfully."},
        #     status=status.HTTP_204_NO_CONTENT,
        # )



# class WishlistApiView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request, pk, *args, **kwargs):
#         post_id = Post.objects.get(pk=pk)
#         user = request.user

#         existing_wishlist = Wishlist.objects.filter(post=post_id, user=user)
#         if existing_wishlist:
#             existing_wishlist.delete()
#             return Response({"msg": "Un_wishlist"}, status=status.HTTP_200_OK)
#         else:
#             serializer = WishlistSerializer(data={"post": post_id.id, "user": user.id})
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response({"msg": "wishlist"}, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class LikedUserApiView(APIView):
#     def get(self, requset, pk , *args, **kwargs):
#         try:
#             user = User.objects.get(pk = pk)
#             liked_post = Like.objects.filter(user=user)
#             serializer = LikeSerializer( liked_post, many = True)
#             return Response(serializer.data , status=status.HTTP_200_OK)
#         except :
#             return Response({'msg':'eorrorr'} , status=status.HTTP_400_BAD_REQUEST)