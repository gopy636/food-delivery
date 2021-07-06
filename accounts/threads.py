import threading, random, uuid
from django.conf import settings
from django.core.mail import send_mail


class send_verification_email(threading.Thread):

    def __init__(self, email,token):
        self.email = email
        self.token = token
        threading.Thread.__init__(self)

    def run(self):
        try:
            subject = "Link to verify the your Account"
            message = f"The Token to verify your email is  activation_url = http://127.0.0.1:8000/accounts/verify/{self.token}/"
            email_from = settings.EMAIL_HOST_USER
            print("Email send initiated")
            send_mail(subject , message ,email_from ,[self.email])
            print("Email has been Sent")
        except Exception as e:
            print(e)




class send_verify_custom_email(threading.Thread):
    
    def __init__(self, email,token):
        self.email = email
        self.token = token
        threading.Thread.__init__(self)

    def run(self):
        try:
            subject = "Link to verify the your Account"
            message = f"The Token to verify your email is  activation_url = http://127.0.0.1:8000/accounts/custom/verify/{self.token}/"
            email_from = settings.EMAIL_HOST_USER
            print("Email send initiated")
            send_mail(subject , message ,email_from ,[self.email])
            print("Email has been Sent")
        except Exception as e:
            print(e)