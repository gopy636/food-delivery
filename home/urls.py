
from django.urls import path
from home.views import *




urlpatterns = [
    
    path('', home),
    path('menu/<slug>/',view_menu, name="restraunt_detail")

]