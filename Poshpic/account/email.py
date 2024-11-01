from django.core.mail import send_mail
import random
from django.conf import settings
from .models import User


def sent_otp_vary_email(email):
    subject = f"Your account verification email for {email}"
    otp = random.randint(1000, 9999)
    message = f"your  otp is  {otp}"
    
    email_from = settings.EMAIL_HOST
    send_mail(subject, message, email_from, [email])
    
     # Save OTP to the user model
    user_obj = User.objects.get(email=email)
    user_obj.otp = otp
    user_obj.save()
