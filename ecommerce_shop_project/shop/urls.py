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
    path("edit_comment/<int:comment_pk>/", views.process_comment, name="edit_comment"),
    path("add_comment/<int:product_pk>/", views.process_comment, name="add_comment"),
    path("about/", views.about, name="about"),
    path("like_product/<product_id>", views.like_product, name="like_product"),
    path("add_rating/<product_id>", views.process_rating, name="add_rating"),
]
