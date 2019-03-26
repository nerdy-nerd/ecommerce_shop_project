from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("product/<int:pk>/", views.product_detail, name="product_detail"),
    path(
        "category/<str:name>/",
        views.CategoryProductView.as_view(),
        name="category_product",
    ),
]
