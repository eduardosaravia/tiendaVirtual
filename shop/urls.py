from django.urls import path
from .views import *

app_name = "shop"

urlpatterns = [
    path('',index, name="index"),
    path('product/<int:pk>/',product_detail,name='product_detail' ),
    path('product/create/',produt_create,name='product_create'),
]