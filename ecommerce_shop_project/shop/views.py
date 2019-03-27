from django.shortcuts import render
from .models import Product
from django.shortcuts import get_object_or_404


def product_list(request):
    products = Product.objects.all()
    for p in products:
        total_rating = int(p.total_rating)
        p.stars = range(total_rating)
        p.empty_stars = range(5 - total_rating)
    context = {"products": products}
    return render(request, "shop/product_list.html", context=context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    total_rating = int(product.total_rating)
    stars = range(total_rating)
    empty_stars = range(5 - total_rating)
    return render(request, "shop/product_detail.html", {"product": product, "stars": stars, "empty_stars": empty_stars})
