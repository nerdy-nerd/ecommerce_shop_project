from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


from django import forms


# class AccountRegisterForm(UserCreationForm):
#     email = forms.EmailField(required=True)

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for fieldname in ["username", "password1", "password2"]:
#             self.fields[fieldname].help_text = None

#     class Meta:
#         model = User
#         fields = ["username", "email", "password1", "password2"]


# class UserUpdateForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ["username", "email", "first_name", "last_name"]


# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ["street", "city", "province", "code", "phone"]
