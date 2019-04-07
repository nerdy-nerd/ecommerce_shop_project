from django.shortcuts import render, redirect, get_object_or_404
# from django.views.decorators.http import require_POST
from cart.cart import Cart
from cart.forms import CartAddProductForm


def cart_data(request):
    cart = Cart(request)
    return render(request, "cart_data.html", {"cart": cart})


