from django.db import models
from account.models import User

class Payment(models.Model):
    PENDING = "pending"
    COMPLETED = "completed"
    STATUS_CHOICES = [
        (PENDING, "Pending"),
        (COMPLETED, "Completed"),
    ]
    Photogarpher = models.ForeignKey(User, on_delete=models.CASCADE)
    month = models.IntegerField()
    year = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    stripe_id = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    expiration_date = models.DateField(null=True, blank=True)
   
    def __str__(self):
        return f" {self.Photogarpher.email} took a subscription on  {self.month}/{self.year}"