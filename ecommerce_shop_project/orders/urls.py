from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    path("create/", views.order_create, name="order_create"),
    path("create/<uuid:address_uuid>/", views.order_create, name="order_create"),
    path("new_address/", views.AddressCreateView.as_view(), name="new_address"),
]
