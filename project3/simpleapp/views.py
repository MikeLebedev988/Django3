# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Products


# Create your views here.
class ProductsList(ListView):
    model = Products
    ordering = 'name'
    # queryset = Products.objects.order_by('-name')
    template_name = 'products.html'
    context_object_name = 'products'


class ProductsDetail(DetailView):
    model = Products
    template_name = 'products.html'
    context_object_name = 'products'
