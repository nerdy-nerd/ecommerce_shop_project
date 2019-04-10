from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserAdminCreationForm

User = get_user_model()


class UserAdmin(BaseUserAdmin):

    add_form = UserAdminCreationForm

    list_display = ("email", "is_admin", "first_name", "last_name")
    list_filter = ("is_admin",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "phone")}),
        ("Adress", {"fields": ("street", "city", "province", "code", "country")}),
        ("Timestamps", {"fields": ("created", "updated")}),
        ("Permissions", {"fields": ("is_active", "is_admin", "is_staff")}),
    )
    readonly_fields = ("created", "updated")

    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),
    )
    search_fields = ("email",)
    ordering = ("email",)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)


# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)
