from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import ModelFormMixin
from django.views.generic import TemplateView, DetailView, FormView, View
from django.db.models import Count
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import get_user_model
from django.views.generic.detail import SingleObjectMixin

from shop import models
from orders.models import Order
from .forms import (
    PublishCommentForm,
    OrderPayForm,
    DiscountProductForm,
    DiscountCategoryForm,
)

User = get_user_model()


class PanelView(TemplateView):
    template_name = "staff/panel.html"


class ProductListView(ListView):
    template_name = "staff/product_list.html"
    context_object_name = "products"
    queryset = (
        models.Product.objects.all()
        .prefetch_related("category")
        .prefetch_related("discounts")
    )


class ProductImageListView(ListView):
    template_name = "staff/product_images_list.html"
    context_object_name = "product_images"
    queryset = models.ProductImage.objects.all().prefetch_related("product")


class CategoryListView(ListView):

    template_name = "staff/category_list.html"
    context_object_name = "categories"
    # add annotation to limit db queries
    queryset = models.Category.objects.all().annotate(prod_count=Count("product"))


class CommentListView(ListView):
    model = models.Comment
    template_name = "staff/comment_list.html"
    context_object_name = "comments"
    ordering = ["-is_new", "-date_created"]
    queryset = models.Comment.objects.all().prefetch_related("product", "user")


class UserListView(ListView):
    model = User
    template_name = "staff/user_list.html"
    context_object_name = "users"


class OrderListView(ListView):
    model = Order
    template_name = "staff/order_list.html"
    context_object_name = "orders"
    queryset = Order.objects.all().prefetch_related("items")


class AddCategoryView(CreateView):
    template_name = "staff/add_category.html"
    model = models.Category
    fields = ["name"]

    def get_success_url(self):
        return reverse("staff:category_list")


class AddProductView(CreateView):
    template_name = "staff/add_product.html"
    model = models.Product
    fields = ["category", "name", "description", "original_price", "stock", "available"]

    def get_success_url(self):
        return reverse("staff:product_list")


class AddProductImageView(CreateView):
    template_name = "staff/add_product_image.html"
    model = models.ProductImage
    fields = ["product", "image"]

    def get_success_url(self):
        return reverse("staff:product_images_list")


class UpdateProductView(UpdateView):
    model = models.Product
    template_name = "staff/update_product.html"
    fields = [
        "category",
        "name",
        "slug",
        "description",
        "original_price",
        "stock",
        "available",
    ]

    def get_success_url(self):
        return reverse("staff:product_list")

    def get_object(self):
        prod = get_object_or_404(models.Product, pk=self.kwargs["pk"])
        return prod


class UpdateProductImageView(UpdateView):
    model = models.Product
    template_name = "staff/update_product_image.html"
    fields = ["name", "image"]

    def get_success_url(self):
        return reverse("staff:product_images_list")

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


class DeleteProductImageView(DeleteView):
    model = models.ProductImage
    template_name = "staff/delete_product_image.html"

    def get_success_url(self):
        return reverse("staff:product_images_list")

    def get_object(self):
        image = get_object_or_404(models.ProductImage, pk=self.kwargs["pk"])
        return image


class DeleteCategoryView(DeleteView):
    model = models.Category
    template_name = "staff/delete_category.html"

    def get_success_url(self):
        return reverse("staff:category_list")

    def get_object(self):
        cat = get_object_or_404(models.Category, pk=self.kwargs["pk"])
        return cat


class CommentDetailView(View):
    def get(self, request, *args, **kwargs):
        view = CommentDetail.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = PublishComment.as_view()
        return view(request, *args, **kwargs)


class CommentDetail(DetailView):
    model = models.Comment
    template_name = "staff/comment_detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["form"] = PublishCommentForm(instance=self.object)
        return context

    def get_object(self):
        self.object = super().get_object()
        self.object.is_new = False
        self.object.save()
        return self.object


class PublishComment(UpdateView):
    template_name = "staff/comment_detail.html"
    form_class = PublishCommentForm
    model = models.Comment

    def get_success_url(self):
        return reverse("staff:comment_list")


class UserDetailView(DetailView):
    model = User
    template_name = "staff/user_detail.html"


def toggle_comment_activity(request, pk):
    comment = get_object_or_404(models.Comment, pk=pk)
    comment.is_active = not comment.is_active
    comment.save()
    return redirect(reverse("staff:comment_list"))


class OrderDetailView(View):
    def get(self, request, *args, **kwargs):
        view = OrderDetail.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = OrderPay.as_view()
        return view(request, *args, **kwargs)


class OrderDetail(DetailView):
    model = Order
    template_name = "staff/order_detail.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.prefetch_related("items")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["form"] = OrderPayForm(instance=self.object)
        return context


class OrderPay(UpdateView):
    form_class = OrderPayForm
    model = Order
    template_name = "staff/order_detail.html"

    def get_success_url(self):
        return reverse("staff:order_list")


def discount_product(request, pk):
    product = get_object_or_404(models.Product, pk=pk)
    discounts = product.discounts.all()
    if request.method == "POST":
        form = DiscountProductForm(request.POST)
        if form.is_valid():
            prod_disc = form.save(commit=False)
            prod_disc.product = product
            prod_disc.save()

            return redirect("staff:product_list")

    else:
        form = DiscountProductForm()

    return render(
        request,
        "staff/discount_product.html",
        {"form": form, "product": product, "discounts": discounts},
    )


def delete_product_discount(request, pk):
    discount = get_object_or_404(models.ProductDiscount, pk=pk)
    prod_pk = discount.product.pk
    discount.delete()
    return redirect("staff:discount_product", prod_pk)


def discount_category(request, pk):
    category = get_object_or_404(models.Category, pk=pk)
    discounts = category.discounts.all()
    if request.method == "POST":
        form = DiscountCategoryForm(request.POST)
        if form.is_valid():
            cat_disc = form.save(commit=False)
            cat_disc.category = category
            cat_disc.save()
            products = category.product_set.all()
            for product in products:
                disc = models.ProductDiscount(
                    product=product,
                    discount_percent=form.cleaned_data["discount_percent"],
                    start_time=form.cleaned_data["start_time"],
                    end_time=form.cleaned_data["end_time"],
                    category_discount=cat_disc,
                )
                disc.save()
            return redirect("staff:category_list")

    else:
        form = DiscountCategoryForm()

    return render(
        request,
        "staff/discount_category.html",
        {"form": form, "category": category, "discounts": discounts},
    )


def delete_category_discount(request, pk):
    discount = get_object_or_404(models.CategoryDiscount, pk=pk)
    cat_pk = discount.category_id
    discount.delete()
    return redirect("staff:discount_category", cat_pk)

