from django.contrib import admin
from chat.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ["username"]


# from . models import ChatMessage

# # Register your models here.

# @admin.register(ChatMessage)
# class ChatAdmin(admin.ModelAdmin):
#     list_editable = ['is_read']
#     list_display = ['user' ,'sender','receiver','message','date' ,'is_read' ]
