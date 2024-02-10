from django.db import models
from  account.models import User 
from datetime import datetime

# Create your models here.
class Follow(models.Model):
    user = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    following_user = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    create_at = models.DateTimeField(default=datetime.now())
    
    
