from django.shortcuts import render
from .models import Product, Category
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.http import HttpResponse


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

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        products = Product.objects.all()
        populate_products_add_ratings(products)
        context["products"] = products

        return context

    def get(self, request, *args, **kwargs):
        query = request.GET.get("q")
        products = Product.objects.all()
        if query:
            products = products.filter(name__contains=query)
        populate_products_add_ratings(products)
        context = super().get_context_data(*args, **kwargs)
        context["query"] = query

        return render(request, self.template_name, context=context)


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
    category_list = Category.objects.all()
    total_rating = int(product.total_rating)
    stars = range(total_rating)
    empty_stars = range(5 - total_rating)
    context = {"product": product, "category_list": category_list, "stars": stars, "empty_stars": empty_stars}
    return render(request, "shop/product_detail.html", context=context)

