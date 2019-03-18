from django.shortcuts import render
from . models import Product


def product_list(request):
    products = Product.objects.filter(available__exct=True)
    context = {"products": products}
    return render(request, 'shop/product_list.html', context=context)
