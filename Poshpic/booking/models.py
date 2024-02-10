from django.db import models
from account.models import User
from datetime import datetime

# Create your models here.


class BookingPhotographer(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
    )

    user = models.ForeignKey(User, related_name='booking_user', on_delete=models.CASCADE)
    photographer = models.ForeignKey(User, related_name='booking_photographer', on_delete=models.CASCADE)
    booking_date = models.DateTimeField(default = datetime.now())
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    booking_status = models.CharField(max_length=50, choices=STATUS_CHOICES,default = 'pending')
    is_completed = models.BooleanField(default=False)
    
    

    
    
    
    
    