from django.shortcuts import get_object_or_404, render

from datetime import date

from .models import Category, Product

def categories(request):
    return{
        'categories': Category.objects.all
    }

def home(request):
    products = Product.objects.all()
    return render(request, 'index.html',{'products': products})

def all(request):
    products = Product.objects.all()
    return render(request, 'all.html',{'products': products})

def about(request):
    return render(request, 'about.html')

def login(request):
    return render(request, 'login.html')

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/product.html', {'product': product})

def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/category.html', {'category': category, 'products': products})