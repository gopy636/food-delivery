from django.http.response import HttpResponse
from django.shortcuts import render,redirect

# Create your views here.
from restaurant.models import *
from .models import *
import uuid


def home(request):
    context = {'restaurants' : Restaurant.objects.all()}
    return render(request,'home/home.html',context)


def view_menu(request, slug):
    try:
        rest_objs=Restaurant.objects.get(id= slug)
        context = {'rest_menu' : rest_objs ,'menus': rest_objs.restaurant.all}
        return render(request,'home/menu.html',context)
    except Exception as e:
        print(e)
        return redirect('/error/')



