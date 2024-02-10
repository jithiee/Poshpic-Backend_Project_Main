from django.contrib import admin
from . models import Post ,Like ,Comment ,PostHistory ,Wishlist


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display =  ['id','created_at','title','description','image'] 
    
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
        list_display =['user','post','created_at']
@admin.register(Comment)
class CommentApiview(admin.ModelAdmin):
    list_display = ['user','post','text','created_at']
  
    
@admin.register(PostHistory)
class PostHistoryAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'user','deleted_at' ,'image' ]
    
@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ['id','post']    
          

