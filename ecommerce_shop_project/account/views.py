from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AccountRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == "POST":
        form = AccountRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, "Account created")
            return redirect("account:login")

    else:
        form = AccountRegisterForm()
    return render(request, "account/register.html", {"form": form})


def profile(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if user_form.is_valid and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {"u_form": user_form, "p_form": profile_form}
    return render(request, "account/profile.html", context=context)

