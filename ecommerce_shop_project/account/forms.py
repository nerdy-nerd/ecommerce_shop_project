from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()


class AccountRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["email", "password1", "password2"]


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email",)


class UserAdminCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "is_staff", "is_admin")

