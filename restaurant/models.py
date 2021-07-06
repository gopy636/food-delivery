
# Create your models here.
from django.db import models
from accounts.models import Shopkeeper
from home.models import BaseModel

class FoodItem(BaseModel):

    '''
    FoodItem model handling Food Type
    '''
    food_item_type = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.food_item_type



class Restaurant(BaseModel):
    '''
    Restaurant model handling Restaurant data
    '''
    shopkeeper = models.OneToOneField(Shopkeeper , related_name='shopkeeper' , on_delete=models.CASCADE)
    restaurant_name = models.CharField(max_length=100)
    restaurant_descripton = models.TextField()
    restaurant_address = models.TextField()
    restaurant_pincode = models.CharField(max_length=100)
    restaurant_rating = models.IntegerField(default=-1)
    lattitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    restraunt_image = models.ImageField(upload_to = 'restaurant')


    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return self.restaurant_name


class RestrauntMenu(BaseModel):
    '''
    RestaurantMenu model handling restaurant menu
    '''
    restaurant = models.ForeignKey(Restaurant , related_name='restaurant' , on_delete=models.CASCADE)
    food_item_type = models.ForeignKey(FoodItem , on_delete=models.SET_NULL , null=True , blank=True)
    menu_price = models.IntegerField()
    menu_name = models.CharField(max_length=100)
    menu_description =models.CharField(max_length=100)
    menu_type = models.CharField(max_length=100 , choices=(('Veg'  , 'Veg') , ('Non Veg' , 'Non Veg')) , default='Veg')
    menu_image = models.ImageField(upload_to='menu')
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.menu_name