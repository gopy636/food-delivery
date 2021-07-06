from django.conf import settings
from django.core.mail import send_mail
import time




def send_activation_email(email ,email_token):
    try:

        subject = 'Your accounts needs to verified'
        message = f'Hi click on the link to activate your account activation_url = http://127.0.0.1:8000/accounts/verify/{email_token}/'
        email_from = settings.EMAIL_HOST
        print('SEND EMAIL STARTED')
        send_mail(subject , message ,email_from ,[email])
        print('EMAIL SENT')


    except Exception as e:
        print(e)



def send_forgt_password_email(email,token):
    try:
        subject = 'Your forgot password link'
        message = f'Hi click on the link to set your new password your link url = http://127.0.0.1:8000/accounts/forgot-password/{token}/'
        email_from = settings.EMAIL_HOST
        print('SEND EMAIL STARTED')
        send_mail(subject , message ,email_from ,[email])
        print('EMAIL SENT')


    except Exception as e:
        print(e)
