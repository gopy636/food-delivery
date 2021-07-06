from django.shortcuts import redirect, render
from .models import *
from accounts.models import *
from .forms import *


def add_restaurant(request):
    context ={}
  
    # create object of form
    form = RestaurantForm(request.POST or None, request.FILES or None)
      
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
        return redirect('../add-menu/')
  
    context['form']= form
    return render(request, "restaurant/addresto.html", context)



def add_menu(request):
    context ={}
  
    # create object of form
    form = RestrauntMenuForm(request.POST or None, request.FILES or None)
      
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
        return redirect('../resto-detail/')
  
    context['form']= form
    return render(request, "restaurant/addresto.html", context)



def resto_detail(request):
    resto_objs=Restaurant.objects.all()
    return render(request,"restaurant/allresto.html",{'resto_objs':resto_objs})