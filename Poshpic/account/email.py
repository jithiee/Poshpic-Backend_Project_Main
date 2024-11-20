from django.core.mail import send_mail
import random
from django.conf import settings
from .models import User
from datetime import datetime 
from django .utils import timezone


def sent_otp_vary_email(email):
    
    user_obj = User.objects.get(email = email)
    user_name = user_obj.username if hasattr(user_obj , "username") else "User"
    subject = f"Your account verification email for {email}"
    otp = random.randint(1000, 9999)
    
    #text message
    message = f"""
    Hi {user_name},

    Thank you for signing up with us! Please use the following One-Time Password (OTP) to verify your email address:

    OTP: {otp}

    If you did not request this email, please ignore it or contact support.

    Regards,
    The Poshpic service  Team
    """
    
    email_from = settings.EMAIL_HOST
    send_mail(
        subject,
        message,
        email_from, 
        [email]
        
        ) 
 
     # Save OTP to the user model
    user_obj = User.objects.get(email=email)
    user_obj.otp = otp
    user_obj.otp_created_at = timezone.now()
    user_obj.save()
