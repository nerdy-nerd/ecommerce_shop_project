from django.urls import path
from .views import (
    PanelView,
    ProductListView,
    CategoryListView,
    CommentListView,
    UserListView,
    OrderListView,
    OrderDetailView,
    AddProductView,
    AddCategoryView,
    UpdateProductView,
    UpdateCategoryView,
    DeleteProductView,
    DeleteCategoryView,
    UserDetailView,
    CommentDetailView,
    toggle_comment_activity,
    discount_product,
    delete_discount,
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
        "comment_list", staff_required(CommentListView.as_view()), name="comment_list"
    ),
    path("order_list", staff_required(OrderListView.as_view()), name="order_list"),
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
    path(
        "delete_discount/<int:pk>/",
        staff_required(delete_discount),
        name="delete_discount",
    ),
    # detail
    path(
        "user_detail/<int:pk>",
        staff_required(UserDetailView.as_view()),
        name="user_detail",
    ),
    path(
        "comment_detail/<int:pk>",
        staff_required(CommentDetailView.as_view()),
        name="comment_detail",
    ),
    path(
        "order_detail/<int:pk>",
        staff_required(OrderDetailView.as_view()),
        name="order_detail",
    ),
    path(
        "comment_detail/<int:pk>",
        staff_required(CommentDetailView.as_view()),
        name="comment_detail",
    ),
    # other
    path(
        "toggle_comment/<int:pk>",
        staff_required(toggle_comment_activity),
        name="toggle_comment",
    ),
    path(
        "discount_product/<int:pk>",
        staff_required(discount_product),
        name="discount_product",
    ),
]
