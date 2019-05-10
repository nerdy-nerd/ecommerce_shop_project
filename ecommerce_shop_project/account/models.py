from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import uuid


class UserManager(BaseUserManager):
    def create_user(
        self, email, password=None, is_active=True, is_staff=False, is_admin=False
    ):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")

        user_obj = self.model(email=self.normalize_email(email))
        user_obj.set_password(password)
        user_obj.is_staff = is_staff
        user_obj.is_admin = is_admin
        user_obj.is_active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password=None):
        user = self.create_user(email, password=password, is_staff=True)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password=password, is_staff=True, is_admin=True)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)  # can login
    is_staff = models.BooleanField(default=False)  # staff user non superuser
    is_admin = models.BooleanField(default=False)  # superuser
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"  # username
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class Address(models.Model):

    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name="addresses", null=True
    )
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, null=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, null=True)
    street = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    province = models.CharField(max_length=100, null=True, blank=True)
    postal_code = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.id} {self.name}  \n \
                {self.street}, {self.city} \n \
                {self.postal_code}, {self.city} \n \
                    {self.country} {self.user}"
