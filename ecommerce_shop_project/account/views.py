from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView

from .forms import AccountRegisterForm, UserUpdateForm
from django.contrib.auth import get_user_model

User = get_user_model()


def register(request):
    if request.method == "POST":
        form = AccountRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, "Account created")
            return redirect("shop:index")

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


def profile(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        if user_form.is_valid:
            user_form.save()

    else:
        user_form = UserUpdateForm(instance=request.user)

    context = {"u_form": user_form}
    return render(request, "account/profile.html", context=context)

