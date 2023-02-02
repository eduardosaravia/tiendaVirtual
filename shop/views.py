from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# GET OBJECT ERROR 404
from django.shortcuts import get_object_or_404
from .models import *

def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        "categories" : categories,
        "products" : products
    }
    return render(request, 'shop/index.html',context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk = pk)
    context = {
        "product" : product
    }
    return render(request,'shop/product_detail.html',context)