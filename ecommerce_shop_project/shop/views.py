from django.shortcuts import render
from .models import Product
from django.shortcuts import get_object_or_404


def product_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "shop/product_list.html", context=context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "shop/product_detail.html", {"product": product})
