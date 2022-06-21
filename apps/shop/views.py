from django.shortcuts import render
from .models import Product, Price
from django.views.generic import ListView, DetailView


class ProductView(ListView):
    template_name = 'shop/shop.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 16

class ProductDetailView(DetailView):
    template_name = 'shop/product-details.html'
    model = Product
    context_object_name = 'product'

# class PriceView(DetailView):
#     template_name = 'shop/product-details.html'
#     model = Price
#     context_object_name = 'price'