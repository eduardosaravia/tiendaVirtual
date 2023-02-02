from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# GET OBJECT ERROR 404
from django.shortcuts import get_object_or_404, redirect
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

def produt_create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        descripcion = request.POST.get('descripcion')
        price = request.POST.get('price')
        category = request.POST.get('category')
        category = Category.objects.get(id=category)
        product = Product.objects.create(
            name = name,
            descripcion = descripcion,
            price = price,
            category = category
        )
        return redirect('shop:product_detail',pk = product.id)

    context ={
        'categories' : Category.objects.all()

    }
    return render(request,'shop/product_create.html',context)