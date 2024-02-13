from django.contrib import admin
from .models import User, PhotographerProfile, Userprofile


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "email", "is_photographer"]
    list_display_links = ["id", "username"]


@admin.register(Userprofile)
class UserprofileAdmn(admin.ModelAdmin):
    list_display = ["id", "city", "country", "address", "profile_image"]


@admin.register(PhotographerProfile)
class PhotographerProfile(admin.ModelAdmin):
    list_display = [
        "id",
        "specialty",
        "experience",
        "city",
        "country",
        "status",
        "address",
        "profile_image",
    ]


# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ['id','photographer','image','created_time','title','description']

# @admin.register(Like)
# class LikeAdmin(admin.ModelAdmin):
#     list_display = ['id','user','post','comment','created_at']

# @admin.register(Wishlist)
# class WishlistAdmin(admin.ModelAdmin):
#     list_display = ['id','post','user','added_time']


# @admin.register(Comment)
# class CommentAdmn(admin.ModelAdmin):
#     list_display = ['id','user','post','text','created_at']


# @admin.register(Rating)
# class RatingAdmin(admin.ModelAdmin):
#     list_display = ['id','user','post','rating']
