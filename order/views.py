from django.shortcuts import render,redirect
from.models import *
from restaurant.models import *
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import sys, os
    
@login_required(login_url='/accounts/cust/login/')
def add_cart(request , menu_id):
    try:
       customer=request.user.customer 
       catr_obj, created=Cart.objects.get_or_create(customer=customer,is_paid=False)
       menu_obj=RestrauntMenu.objects.get(id=menu_id)
       print(catr_obj)
       if catr_obj.cart.filter(restraunt_menu=menu_obj).exists():
           cart_item_obj=CartItems.objects.get(cart=catr_obj,restraunt_menu=menu_obj)
           cart_item_obj.quantity +=1
           cart_item_obj.save()
       else:
           CartItems.objects.create(
               cart=catr_obj,
               restraunt_menu=menu_obj
               )
               
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        print(e)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/accounts/cust/login/')
def remove_cart(request , menu_id):
    try:
       customer=request.user.customer 
       catr_obj=Cart.objects.get(customer=customer,is_paid=False)
       menu_obj=RestrauntMenu.objects.get(id=menu_id)
       print(menu_obj)
       if catr_obj.cart.filter(restraunt_menu=menu_obj).exists():
           cart_item_obj=CartItems.objects.get(cart=catr_obj,restraunt_menu=menu_obj)
           cart_item_obj.quantity -=1
           cart_item_obj.save()
           print(cart_item_obj)
       else:
           CartItems.objects.filter(
               cart=catr_obj,
               restraunt_menu=menu_obj
               ).delete()
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        print(e)
        

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def get_total(request):
    total_price=0.00
    customer=request.user.customer
    catr_obj=Cart.objects.get(customer=customer,is_paid=False)
    cart_item_obj=CartItems.objects.get(catr_obj='cart_id')
    print(cart_item_obj)
    for item in cart_item_obj():
       cart_price= (item.restraunt_menu)*(item.quantity)
       total_price=cart_price
       total_price=total_price+cart_price
    print(total_price)
    
