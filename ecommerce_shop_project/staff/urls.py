from django.urls import path
from .views import (
    PanelView,
    ProductListView,
    CategoryListView,
    CommentListView,
    UserListView,
    AddProductView,
    AddCategoryView,
    UpdateProductView,
    UpdateCategoryView,
    DeleteProductView,
    DeleteCategoryView,
)
from .decorators import staff_required

app_name = "staff"
urlpatterns = [
    path("", staff_required(PanelView.as_view()), name="panel"),
    # list
    path(
        "product_list", staff_required(ProductListView.as_view()), name="product_list"
    ),
    path(
        "categories_list",
        staff_required(CategoryListView.as_view()),
        name="category_list",
    ),
    path(
        "comments_list", staff_required(CommentListView.as_view()), name="comment_list"
    ),
    path("user_list", staff_required(UserListView.as_view()), name="user_list"),
    # add
    path("add_product", staff_required(AddProductView.as_view()), name="add_product"),
    path(
        "add_category", staff_required(AddCategoryView.as_view()), name="add_category"
    ),
    # edit
    path(
        "update_product/<int:pk>",
        staff_required(UpdateProductView.as_view()),
        name="update_product",
    ),
    path(
        "update_category/<int:pk>",
        staff_required(UpdateCategoryView.as_view()),
        name="update_category",
    ),
    # delete
    path(
        "delete_product/<int:pk>",
        staff_required(DeleteProductView.as_view()),
        name="delete_product",
    ),
    path(
        "delete_category/<int:pk>",
        staff_required(DeleteCategoryView.as_view()),
        name="delete_category",
    ),
]

