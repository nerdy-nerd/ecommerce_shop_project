from django.urls import path
from . import views

urlpatterns = [
    path("panel/", views.PanelView.as_view(), name="panel"),
    path("add_product", views.AddProductView.as_view(), name="add_product"),
]

