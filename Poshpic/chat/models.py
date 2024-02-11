from django.db import models
from booking.models import BookingPhotographer




class Room(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Message(models.Model):
    room_name = models.ForeignKey(BookingPhotographer, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to="uploads/", null=True, blank=True)
    
    class Meta:
        db_table = "chat_message"
        ordering = ('timestamp',)
    
    
    
    











































# from account.models import User , Userprofile
# from datetime import datetime

# class ChatMessage(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
#     sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
#     receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")
    
#     message = models.CharField(max_length=1000)
#     is_read = models.BooleanField(default=False)
#     date = models.DateTimeField(default=datetime.now())
    
#     class Meta:
#         ordering = ['date']
#         verbose_name_plural = "Messages"

#     def __str__(self):
#         return f"{self.sender} - {self.receiver}"
   
#     @property 
#     def sender_profile(self):
#         sender_profile = Userprofile.objects.get(user = self.sender)
#         return sender_profile
    
#     @property 
#     def receiver_profile(self):
#         receiver_profile = Userprofile.objects.get(user = self.receiver)
#         return receiver_profile
