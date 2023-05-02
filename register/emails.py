from django.core.mail import send_mail
import random
from django.conf import settings
from .models import User



def send_otp(email):
    subject = 'ACCOUNT VERIFICATION'
    otp = random.randint(1000, 9999) #This will generate random otp
    message = f'Your OTP is {otp}'
    email_from = settings.EMAIL_HOST
    send_mail(subject,message,email_from,[email])
    user_obj = User.objects.get(email=email)
    user_obj.otp = otp
    user_obj.save()
 


