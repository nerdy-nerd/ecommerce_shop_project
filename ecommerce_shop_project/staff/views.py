from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from shop import models
from django.db.models import Count
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class PanelView(TemplateView):
    template_name = "staff/panel.html"


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


class AddCategoryView(CreateView):
    template_name = "staff/add_category.html"
    model = models.Category
    fields = ["name"]

    def get_success_url(self):
        return reverse("staff:category_list")


class AddProductView(CreateView):
    template_name = "staff/add_product.html"
    model = models.Product
    fields = [
        "category",
        "name",
        "slug",
        "description",
        "price",
        "stock",
        "available",
        "image",
    ]

    def get_success_url(self):
        return reverse("staff:product_list")


class UpdateProductView(UpdateView):
    model = models.Product
    template_name = "staff/update_product.html"
    fields = [
        "category",
        "name",
        "slug",
        "description",
        "price",
        "stock",
        "available",
        "image",
    ]

    def get_success_url(self):
        return reverse("staff:product_list")

    def get_object(self):
        prod = get_object_or_404(models.Product, pk=self.kwargs["pk"])
        return prod


class UpdateCategoryView(UpdateView):
    model = models.Category
    template_name = "staff/update_category.html"
    fields = ["name"]

    def get_success_url(self):
        return reverse("staff:category_list")

    def get_object(self):
        cat = get_object_or_404(models.Category, pk=self.kwargs["pk"])
        return cat


class DeleteProductView(DeleteView):
    model = models.Product
    template_name = "staff/delete_product.html"

    def get_success_url(self):
        return reverse("staff:product_list")

    def get_object(self):
        prod = get_object_or_404(models.Product, pk=self.kwargs["pk"])
        return prod


class DeleteCategoryView(DeleteView):
    model = models.Category
    template_name = "staff/delete_category.html"

    def get_success_url(self):
        return reverse("staff:category_list")

    def get_object(self):
        cat = get_object_or_404(models.Category, pk=self.kwargs["pk"])
        return cat
