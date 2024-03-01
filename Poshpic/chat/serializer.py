from rest_framework import serializers
from .models import Message
from django.contrib.auth import get_user_model


# class UserGetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = get_user_model()
#         fields = ["email", "username", "id"]
#         extra_kwargs = {"id": {"read_only": True}}


from rest_framework import serializers
from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ("id", "username", "message", "timestamp")
        read_only_fields = ("id", "timestamp")


# class RoomSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Room
#         fields = '__all__'


# class ChatMessageSerializer(serializers.ModelSerializer):
#     receiver_profile = Userserializer(read_only = True)
#     sender_profile = Userserializer(read_only = True)
#     class Meta:
#         model = ChatMessage
#         fields  =  ['user' ,'sender','sender_profile' , 'receiver', 'receiver_profile' ,   'message','date' ,'is_read' ]
