from django.contrib import admin
from .models import Product, Category, Comment, Rating, Like, ProductDiscount


admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(Like)
admin.site.register(ProductDiscount)
