from django.urls import path
from . import views

app_name = "staff"
urlpatterns = [
    path("", views.PanelView.as_view(), name="panel"),
    # list
    path("product_list", views.ProductListView.as_view(), name="product_list"),
    path("categories_list", views.CategoryListView.as_view(), name="category_list"),
    path("comments_list", views.CommentListView.as_view(), name="comment_list"),
    path("user_list", views.UserListView.as_view(), name="user_list"),
    # add
    path("add_product", views.AddProductView.as_view(), name="add_product"),
    path("add_category", views.AddCategoryView.as_view(), name="add_category"),
    # edit
    path(
        "update_product/<int:pk>",
        views.UpdateProductView.as_view(),
        name="update_product",
    ),
    path(
        "update_category/<int:pk>",
        views.UpdateCategoryView.as_view(),
        name="update_category",
    ),
]

