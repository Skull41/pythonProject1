from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def sale(request):
    context= {}
    return render(request, "offers.html", context)


def cart(request):
    context = {}
    return render(request,'cart.html',context)


def checkout(request):
    context = {}
    return render(request,'checkout.html',context)



