from django.db import models
from django.utils import timezone
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=150, db_index=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', default="")
    total_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    count_rating = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ("name",)

    def get_absolute_url(self):
        return reverse("shop:product_detail", args=[str(self.id)])

    def __str__(self):
        return self.name
