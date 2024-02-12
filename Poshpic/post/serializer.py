from rest_framework import serializers
from  .models import Post , Like , Comment , Wishlist


    
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = [ 'user','post','created_at']
    
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [ 'id', 'user','post','text','created_at']

class PostHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [ 'id','user','image','created_at','title','description']
        
        
class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = [ 'id' ,'post', 'user' ,'create_at']   
        
        
         
class PostSerializer(serializers.ModelSerializer):
    likes = LikeSerializer(read_only=True,many=True)
    comments =CommentSerializer(many=True,read_only=True)
    class Meta:
        model = Post
        fields = ["id",'image','created_at','title','description','likes','comments', 'user'] 
        read_only_fields = ['user']
        
    
    def create(self, validated_data):
        posts = Post.objects.create( **validated_data)
        return posts
       

        
