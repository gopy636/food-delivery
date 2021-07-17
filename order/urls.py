
from django.urls import path,include
from .models import *
from .views import *

urlpatterns = [
    path('add-cart/<menu_id>/', add_cart,name="add_cart"),
    path('remove-cart/<menu_id>/',remove_cart,name="remove-cart"),
    path('get-total/',get_total)
]
