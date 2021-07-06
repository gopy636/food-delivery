from django.urls import path
from accounts.views import *


urlpatterns = [
    
    path('customer-register/', customer_register,name='custm-profile'),
    path('shopkeeper-profile/',Shopkeeper_profile,name='shop-profile'),
    path('verify/<token>/',verify_shopkeeper_account,name='verify-shopkeeper'),
    path('login/',login_shopkeeper,name='login-shopkeeper'),
    path('forgot-password/', forget_password),
    path('custom/verify/<token>/',verify_customer_account,name='verify-customer'),
    path('cust/login/',login_customer,name='login-customer')
]