from django.urls import path
from . import views

app_name = "account"
urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", views.UserLogoutView.as_view(), name="logout"),
    path("profile/", views.profile, name="profile"),
    path("profile_edit/", views.ProfileUpdateView.as_view(), name="profile_edit"),
]
