from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from store.models import Product
from .cart import Cart

# Create your views here.

def cart_summary(request):
    return render(request, 'cart/summary.html')

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        # product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product)
        response = JsonResponse({'test':'data'})
        return response
        # cart.add(product=product, qty=product_qty)
        # cartqty = cart.__len__()
        # response = JsonResponse({'qty': cartqty})
        # return response