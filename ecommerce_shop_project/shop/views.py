from django.shortcuts import render, redirect
from .models import Product, Category, Comment
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from cart.forms import CartAddProductForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, resolve
from django.views.decorators.http import require_POST


from .forms import CommentForm


def populate_products_add_ratings(products):
    for p in products:
        total_rating = int(p.total_rating)
        p.stars = range(total_rating)
        p.empty_stars = range(5 - total_rating)
    return products


class IndexView(ListView):

    model = Category
    template_name = "shop/index.html"
    context_object_name = "category_list"

    def post(self, *args, **kwargs):
        return self.get(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        query = self.request.GET.get("q")
        products = Product.objects.all()
        if query:
            products = products.filter(name__contains=query)
        populate_products_add_ratings(products)
        context["products"] = products
        context["query"] = query

        return context


class CategoryProductView(ListView):

    template_name = "shop/category_products.html"
    context_object_name = "products"

    def get_queryset(self):
        self.category = get_object_or_404(Category, name=self.kwargs["name"])
        products = self.category.product_set.all()
        populate_products_add_ratings(products)
        return products

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["category_list"] = Category.objects.all()
        context["category"] = self.category
        return context


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart_product_form = CartAddProductForm()
    category_list = Category.objects.all()

    # star rating
    total_rating = int(product.total_rating)
    stars = range(total_rating)
    empty_stars = range(5 - total_rating)
    # comments
    comments = product.comment_set.filter(active=True)

    form = CommentForm()

    context = {
        "product": product,
        "category_list": category_list,
        "stars": stars,
        "empty_stars": empty_stars,
        "comments": comments,
        "form": form,
        "cart_product_form": cart_product_form,
    }
    return render(request, "shop/product_detail.html", context=context)


@login_required(login_url=reverse_lazy("shop:login"))
@require_POST
def add_comment(request, product_pk=None, comment_pk=None):
    form = CommentForm(request.POST)
    if form.is_valid():
        if product_pk:
            product = get_object_or_404(Product, pk=product_pk)

            new_comment = form.save(commit=False)
            new_comment.product = product
            new_comment.user = request.user
            new_comment.save()
        else:
            comment = get_object_or_404(Comment, pk=comment_pk)
            form = CommentForm(request.POST, instance=comment)
            form.save()
            product = comment.product

        # after submin redirect to porduct page
    return redirect(product)  # same as product.get_absolute_url
