from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import Http404
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.views.generic import UpdateView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import AccountRegisterForm, UserUpdateForm
from django.contrib.auth import get_user_model

from orders.models import Order
from .models import Address

User = get_user_model()


def register(request):
    if request.method == "POST":
        form = AccountRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("account:login")

    else:
        form = AccountRegisterForm()
    return render(request, "account/register.html", {"form": form})


class UserLoginView(LoginView):
    template_name = "account/login.html"

    class Meta:
        model = User


class UserLogoutView(LogoutView):
    template_name = "account/logout.html"

    class Meta:
        model = User


@login_required
def profile(request):
    return render(request, "account/profile.html")


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "account/profile_edit.html"
    form_class = UserUpdateForm
    success_url = reverse_lazy("account:profile")
    login_url = reverse_lazy("account:login")
    # redirect_field_name = "redirect_to"

    def get_object(self):
        user = User.objects.get(pk=self.request.user.id)
        return user


class AccountPasswordChangeView(PasswordChangeView):

    success_url = reverse_lazy("account:profile")
    template_name = "account/password_change_form.html"


class AccountPasswordResetView(PasswordResetView):

    template_name = "account/password_reset_form.html"
    success_url = reverse_lazy("account:password_reset_done")
    email_template_name = "account/password_reset_email.html"


class AccountPasswordResetDoneView(PasswordResetDoneView):

    template_name = "account/password_reset_done.html"


class AccountPasswordResetConfirm(PasswordResetConfirmView):

    success_url = reverse_lazy("account:password_reset_complete")
    template_name = "account/password_reset_confirm.html"


class AccoutnPasswordResetCompleteView(PasswordResetCompleteView):

    template_name = "account/password_reset_complete.html"


@login_required
def order_detail(request, pk):
    get_object_or_404(request.user.orders, pk=pk)
    if not request.user.orders.filter(pk=pk).exists():
        raise Http404()
    order = Order.objects.prefetch_related("items").get(pk=pk)
    # total_cost = order.get_total_cost()
    context = {"order": order}
    return render(request, "account/order_detail.html", context=context)
