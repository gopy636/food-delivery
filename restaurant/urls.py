from django.urls import path
from restaurant.views import *


urlpatterns = [
    
    path('add-restaurant/',add_restaurant,name='add-resto'),
    path('add-menu/',add_menu,name='add-restomenu'),
    path('resto-detail/',resto_detail,name='resto-detail'),
    path('restolist/',RestaurantListView.as_view(),name='restaurant-list'),
    path('menu_detail/',restaurant_menu_detail,name='menu-detail')
]