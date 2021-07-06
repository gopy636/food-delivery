from django.db import models
from django.contrib.auth.models import User
from home.models import BaseModel
from django.db.models.signals import post_save
from django.dispatch import receiver
from .threads import *
class Shopkeeper(User):
    '''
    Shopkeeper model handling restraunt owner
    '''
    phone_number = models.CharField(max_length=10)
    email_token = models.CharField(max_length=100, null=True,blank=True)
    email_verified = models.BooleanField(default=False)
    adhar_card = models.CharField(max_length=16)
    gst_number = models.CharField(max_length=100)
    forgot_token = models.CharField(max_length=100, null=True,blank=True)
    gender = models.CharField(max_length=10,
                choices=(('Male' , 'Male'),
                ('Female' , 'Female')))


    class Meta:
        db_table = 'shopkeeper'
    
    def __str__(self):
        return self.email
@receiver(post_save, sender=Shopkeeper)
def send_mail(sender,instance,created, **kwargs):
    if created:
        emailID = instance.email
        email_token=instance.email_token
        thread_obj = send_verification_email(emailID,email_token)
        thread_obj.start()


class Customer(User):
    '''
    Customer model handling customer
    '''
    phone_number = models.CharField(max_length=10)
    email_token = models.CharField(max_length=100, null=True,blank=True)
    email_verified = models.BooleanField(default=False)
    forgot_token = models.CharField(max_length=100, null=True,blank=True)

    class Meta:
        db_table = 'Customer'

@receiver(post_save, sender=Customer)
def send_mail(sender,instance,created, **kwargs):
    if created:
        emailID = instance.email
        email_token=instance.email_token
        thread_obj = send_verify_custom_email(emailID,email_token)
        thread_obj.start()

    
class CustomerAddress(BaseModel):
    '''
    CustomerAddress model handling Customer Adress
    '''
    customer = models.ForeignKey(Customer, related_name='customer', on_delete=models.CASCADE)
    address = models.TextField()
    pincode = models.CharField(max_length=100)

    