from django.shortcuts import render
from .models import Product
from django.http import HttpResponse


def product_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "shop/product_list.html", context=context)
