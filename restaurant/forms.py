from django.forms import ModelForm
from.models import *

class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'

class RestrauntMenuForm(ModelForm):

    class Meta:

        model = RestrauntMenu
        fields = '__all__'