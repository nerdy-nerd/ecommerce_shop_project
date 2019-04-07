from django.urls import path
from . import views

app_name = "dynamic_cart"

urlpatterns = [
    path("", views.cart_data, name="cart_data"),
]