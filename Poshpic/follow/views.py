from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import FollowSerializer
from account.models import User
from .models import Follow
from rest_framework.response import Response
from rest_framework import status


class FollowApiView(APIView):
    def post(self, request, pk=None, *args, **kwargs):
        user = request.user
        following_user = User.objects.get(id=pk)
        existing_follow = Follow.objects.filter(
            user=user, following_user=following_user
        )

        if existing_follow:
            existing_follow.delete()
            return Response({"msg": "Unfollow"}, status=status.HTTP_200_OK)
        else:
            user = user.id
            following_user = following_user.id
            serializer = FollowSerializer(
                data={"user": user, "following_user": following_user}
            )

            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user)
                return Response({"msg": "Follow"}, status=status.HTTP_201_CREATED)

    # A user following phototgraphers  ====> followings
    def get(self, request, pk, *args, **kwargs):
        try:
            photographer = User.objects.get(pk=pk)
            followers = Follow.objects.filter(user=photographer)
            serializer = FollowSerializer(followers, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"msg": "user not found"}, status=status.HTTP_404_NOT_FOUND)
        except Follow.DoesNotExist:
            return Response(
                {"msg": "No followers found for the user"},
                status=status.HTTP_404_NOT_FOUND,
            )


#   # A photographers followers   <=====
# class PhotographerFollowers(APIView):
#     def get(self, request, pk, *args, **kwargs):
#         try:
#             photographer = User.objects.get(pk=pk)
#             followers = photographer.followers.all()  # Useing  'followers' reverse relation
#             # followers = User.objects.prefetch_related('followers').filter(pk=pk).first().followers.all()
#             serializer = FollowSerializer(followers, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except User.DoesNotExist:
#             return Response({"msg": "photographer not found"}, status=status.HTTP_404_NOT_FOUND)
