from django.shortcuts import render, reverse
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from shop import models
from django.db.models import Count
from django.views.generic.edit import CreateView
from . import forms
from django.http import HttpResponse


class PanelView(TemplateView):
    template_name = "staff/panel.html"


class AddProductView(CreateView):
    template_name = "staff/add_product.html"
    form_class = forms.ProductForm

    def get_success_url(self):
        return reverse("staff:product_list")


class ProductListView(ListView):
    model = models.Product
    template_name = "staff/product_list.html"
    context_object_name = "products"


class CategoryListView(ListView):

    template_name = "staff/category_list.html"
    context_object_name = "categories"
    # add annotation to limit db queries
    queryset = models.Category.objects.all().annotate(prod_count=Count("product"))


class CommentListView(ListView):
    template_name = "TEMPLATE_NAME"


class UserListView(ListView):
    template_name = "TEMPLATE_NAME"
