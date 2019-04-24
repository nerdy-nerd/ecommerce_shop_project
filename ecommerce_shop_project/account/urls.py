from django.urls import path

from .views import (
    register,
    UserLoginView,
    UserLogoutView,
    profile,
    ProfileUpdateView,
    AccountPasswordChangeView,
    AccountPasswordResetView,
    AccountPasswordResetDoneView,
    AccountPasswordResetConfirm,
    AccoutnPasswordResetCompleteView,
    order_detail,
)

app_name = "account"
urlpatterns = [
    path("register/", register, name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    # profile
    path("profile/", profile, name="profile"),
    path("profile_edit/", ProfileUpdateView.as_view(), name="profile_edit"),
    path(
        "password_change/", AccountPasswordChangeView.as_view(), name="password_change"
    ),
    # password reset
    path("password_reset/", AccountPasswordResetView.as_view(), name="password_reset"),
    path(
        "password_reset/done/",
        AccountPasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "password_reset/confirm/<uidb64>/<token>/",
        AccountPasswordResetConfirm.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "password_reset/complete/",
        AccoutnPasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path("order_detail/<int:pk>", order_detail, name="order_detail"),
]
