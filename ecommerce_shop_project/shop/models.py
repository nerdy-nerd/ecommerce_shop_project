from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.text import slugify

from django.conf import settings

import datetime

User = get_user_model()


TIME_DELTA_TO_COMMENT_EDITION = datetime.timedelta(
    seconds=settings.TIME_TO_EDIT_COMMENT_IN_SECONDS
)


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:category_product", args=[str(self.name)])


class Product(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=150, db_index=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )
    image = models.ImageField(upload_to="images/", default="")
    total_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    count_rating = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ("name",)

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug

        ind = 1
        while Product.objects.filter(slug=unique_slug).exists():
            unique_slug += "-{}".format(ind)
            ind += 1

        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("shop:product_detail", args=[str(self.id)])

    def __str__(self):
        return self.name


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    is_new = models.BooleanField(default=True)

    class Meta:
        ordering = ["date_created"]

    def is_editable(self):
        return timezone.now() - self.created < TIME_DELTA_TO_COMMENT_EDITION

    def __str__(self):
        return "Comment from {} related to {}".format(self.user, self.product)

    def get_absolute_url(self):
        return reverse("shop:edit_comment", kwargs={"comment_pk": int(self.id)})
