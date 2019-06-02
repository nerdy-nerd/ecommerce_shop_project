from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product, Category, Comment, Rating, Like
from cart.forms import CartAddProductForm
from .forms import CommentForm
from django.http import JsonResponse


OBJECTS_PER_PAGE = 2


def populate_products_add_ratings(products):
    for product in products:
        stars, empty_stars = count_stars(product)
        product.stars = range(stars)
        product.empty_stars = range(empty_stars)
    return products


def count_stars(product):
    # star rating
    if product.count_rating:
        rating = int(product.total_rating / product.count_rating)
        return rating, 5 - rating
    return 0, 5


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

        page = self.request.GET.get("page", 1)
        paginator = Paginator(products, OBJECTS_PER_PAGE)

        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        populate_products_add_ratings(products)
        context["products"] = products
        context["query"] = query

        return context


class CategoryProductView(ListView):
    template_name = "shop/category_products.html"
    context_object_name = "products"
    paginate_by = OBJECTS_PER_PAGE

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


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    cart_product_form = CartAddProductForm()
    category_list = Category.objects.all()
    # comments
    comments = product.comment_set.all().prefetch_related("user")
    likes = product.likes
    stars, empty_stars = count_stars(product)
    form = CommentForm()
    context = {
        "product": product,
        "category_list": category_list,
        "stars": range(stars),
        "empty_stars": range(empty_stars),
        "comments": comments,
        "form": form,
        "rating": stars,
        "cart_product_form": cart_product_form,
        "likes": likes,
    }
    return render(request, "shop/product_detail.html", context=context)


def about(request):
    category_list = Category.objects.all()
    cart_product_form = CartAddProductForm()
    context = {"category_list": category_list, "cart_product_form": cart_product_form}
    return render(request, "shop/about.html", context=context)


@login_required
@require_POST
def process_comment(request, product_pk=None, comment_pk=None):
    form = CommentForm(request.POST)
    if form.is_valid():
        print("valid")
        if product_pk:
            product = get_object_or_404(Product, pk=product_pk)

            new_comment = form.save(commit=False)
            new_comment.product = product
            new_comment.user = request.user
            new_comment.save()
        elif comment_pk:
            comment = get_object_or_404(Comment, pk=comment_pk)
            form = CommentForm(request.POST, instance=comment)
            form.save()
            product = comment.product

        # after submin redirect to porduct page
    return redirect(product)  # same as product.get_absolute_url


@login_required
@csrf_exempt
def process_rating(request, product_id, stars):
    product = get_object_or_404(Product, id=product_id)
    user = request.user
    if not Rating.objects.filter(product=product, user=user).exists():
        product.total_rating += stars + 1
        product.count_rating += 1
        product.save()
        Rating.objects.create(product=product, user=user)
    stars, _ = count_stars(product)
    return JsonResponse({"stars": stars})


@login_required
@csrf_exempt
def like_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user
    likes = product.likes
    if not Like.objects.filter(product=product, user=user).exists():
        likes = likes + 1
        product.likes = likes
        product.save()
        Like.objects.create(product=product, user=user)
    return HttpResponse(likes)
