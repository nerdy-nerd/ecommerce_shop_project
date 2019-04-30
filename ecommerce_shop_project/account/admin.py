from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserAdminCreationForm

User = get_user_model()


class UserAdmin(BaseUserAdmin):

    add_form = UserAdminCreationForm

    list_display = ("email", "is_admin")
    list_filter = ("is_admin",)
    readonly_fields = ("created", "updated")
    search_fields = ("email",)
    ordering = ("email",)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)


# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)
