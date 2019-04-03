from django.urls import path
from shop.views import IndexView

urlpatterns = [path("", IndexView.as_view(), name="product_list")]
