from rest_framework import generics
from .models import Message
from .serializer import MessageSerializer


class MessageList(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    ordering = ("-timestamp",)

