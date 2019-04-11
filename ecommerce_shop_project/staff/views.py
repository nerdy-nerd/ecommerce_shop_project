from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic import TemplateView, DetailView
from django.db.models import Count
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import get_user_model
from shop import models
from orders.models import Order


User = get_user_model()


class PanelView(TemplateView):
    template_name = "staff/panel.html"


class ProductListView(ListView):
    template_name = "staff/product_list.html"
    context_object_name = "products"
    queryset = models.Product.objects.all().prefetch_related("category")


class CategoryListView(ListView):

    template_name = "staff/category_list.html"
    context_object_name = "categories"
    # add annotation to limit db queries
    queryset = models.Category.objects.all().annotate(prod_count=Count("product"))


class CommentListView(ListView):
    model = models.Comment
    template_name = "staff/comment_list.html"
    context_object_name = "comments"
    ordering = ["-created", "active"]
    queryset = models.Comment.objects.all().prefetch_related("product", "user")


class UserListView(ListView):
    model = User
    template_name = "staff/user_list.html"
    context_object_name = "users"


class AddCategoryView(CreateView):
    template_name = "staff/add_category.html"
    model = models.Category
    fields = ["name"]

    def get_success_url(self):
        return reverse("staff:category_list")


class AddProductView(CreateView):
    template_name = "staff/add_product.html"
    model = models.Product
    fields = ["category", "name", "description", "price", "stock", "available", "image"]

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


def toggle_comment_activity(request, pk):
    comment = get_object_or_404(models.Comment, pk=pk)
    comment.active = not comment.active
    comment.save()
    return redirect(reverse("staff:comment_list"))


class UserDetailView(DetailView):
    model = User
    template_name = "staff/user_detail.html"


class OrderListView(ListView):
    template_name = "staff/order_list.html"
    context_object_name = "orders"
    queryset = Order.objects.all()
