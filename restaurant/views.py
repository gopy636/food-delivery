from django.shortcuts import redirect, render
from .models import *
from accounts.models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,)

@login_required(login_url='/accounts/login/')
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


@login_required(login_url='/accounts/login/')
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



@login_required(login_url='/accounts/login/')
def resto_detail(request,):
    user=Restaurant.objects.all()
    data = request.user 
    return render(request, 'restaurant/restodetail.html', {'user' : user, 'data':data})




class RestaurantListView(LoginRequiredMixin,ListView):
    resto_objs=Restaurant.objects.all()

    model = Restaurant
    template_name = 'restaurant/restodetail.html'
    context_object_name = 'resto_objs'
    
    def get_queryset(self):
        return Restaurant.objects.all().filter(shopkeeper=self.request.user)


def restaurant_menu_detail(request):
    resto_menu=RestrauntMenu.objects.all()
    return render(request,'restaurant/menudetail.html',{'resto_menu': resto_menu})
    