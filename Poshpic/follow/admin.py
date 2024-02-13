from django.contrib import admin
from .models import Follow


# Register your models here.
@admin.register(Follow)
class FolowAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "following_user", "create_at"]
