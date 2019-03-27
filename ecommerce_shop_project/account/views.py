from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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


# def profile(request):
#     if request.method == "POST":
#         user_form = UserUpdateForm(request.POST, instance=request.user)
#         if user_form.is_valid:
#             user_form.save()

#     else:
#         user_form = UserUpdateForm(instance=request.user)

#     context = {"u_form": user_form}
#     return render(request, "account/profile.html", context=context)


@login_required(login_url=reverse_lazy("account:login"))
def profile(request):
    user = get_object_or_404(User, pk=request.user.pk)
    context = {"user": user, "profile_page": True}
    return render(request, "account/profile.html", context=context)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "account/profile_edit.html"
    form_class = UserUpdateForm
    success_url = reverse_lazy("account:profile")
    login_url = reverse_lazy("account:login")
    # redirect_field_name = "redirect_to"

    def get_object(self):
        user = User.objects.get(pk=self.request.user.id)
        return user
