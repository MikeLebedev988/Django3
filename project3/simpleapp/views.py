# from django.shortcuts import render
from datetime import datetime
from pprint import pprint

from django.views.generic import ListView, DetailView
from .models import Products


# Create your views here.
class ProductsList(ListView):
    model = Products
    ordering = 'name'
    # queryset = Products.objects.order_by('-name')
    template_name = 'products.html'
    context_object_name = 'products'

    # Метод get_context_data позволяет нам изменить набор данных,
    # который будет передан в шаблон.
    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['time_now'] = datetime.utcnow()
        # Добавим ещё одну пустую переменную,
        # чтобы на её примере рассмотреть работу ещё одного фильтра.
        context['next_sale'] = None
        return context


class ProductsDetail(DetailView):
    model = Products
    template_name = 'products.html'
    context_object_name = 'products'
