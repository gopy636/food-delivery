
# Register your models here.
from django.contrib import admin
from .models import *


@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    pass

class RestrauntMenuAdmin(admin.StackedInline):
    model = RestrauntMenu


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    inlines = [ RestrauntMenuAdmin ]
