from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    is_photographer = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)
    otp = models.CharField(max_length=4, null=True)
    otp_created_at = models.DateTimeField( null= True , blank= True) # Timestamp for OTP creation

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return f"{self.email}{self.id}"


class Userprofile(models.Model):

    user = models.OneToOneField(
        User, related_name="userprofile", on_delete=models.CASCADE
    )
    city = models.CharField(max_length=50, null=True, blank=True)
    phone = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(
        upload_to="profileimage/",
        height_field=None,
        width_field=None,
        max_length=None,
        null=True,
        blank=True,
    )


class PhotographerProfile(models.Model):
    SPECIALTY_CHOICES = (
        ("portrait", "Portrait Photography"),
        ("landscape", "Landscape Photography"),
        ("wedding ", "Wedding Photography"),
        ("wildlife", "Wildlife Photography"),
        ("fashion", "Fashion Photography"),
        ("sports", "Sports Photography"),
        ("macro", "Macro Photography"),
        ("architectural", "Architectural Photography"),
        ("event", "Event Photography"),
        ("product", "Product Photography"),
        ("food", "Food Photography"),
        ("street", "Street Photography"),
    )

    user = models.OneToOneField(
        User, related_name="photographerprofile", on_delete=models.CASCADE
    )
    specialty = models.CharField(max_length=20, choices=SPECIALTY_CHOICES)
    experience = models.IntegerField(null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    status = models.BooleanField(default=False)
    address = models.TextField(null=True, blank=True)
    phone = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=6, decimal_places=2 , null=True , blank=True)
 
    profile_image = models.ImageField(
        upload_to=None,
        height_field=None,
        width_field=None,
        max_length=None,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.id}"
