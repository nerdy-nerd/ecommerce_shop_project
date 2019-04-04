from django.forms import ModelForm
from shop import models


class ProductForm(ModelForm):
    class Meta:
        model = models.Product
        fields = [
            "category",
            "name",
            "slug",
            "description",
            "price",
            "stock",
            "available",
            "image",
        ]

