from django.urls import path
from . import views

app_name = "subscription"

urlpatterns = [
    path("", views.subscription, name="subscription"),
    path("success/", views.success_view, name="success"),
]
