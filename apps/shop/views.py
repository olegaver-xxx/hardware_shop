from django.shortcuts import render
from .models import Product
from django.views.generic import ListView


class ProductView(ListView):
    template_name = 'shop/product_list.html'
    model = Product
    context_object_name = 'product'
