from django.shortcuts import render

from .models import Category, Product

def all_products(request):
    #products = Product.objects.all()
    return render(request, 'store/home.html') 
                  #{'products': products})

def products(request):
    return render(request, "store/products.html")