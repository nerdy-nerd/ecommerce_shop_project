from django import forms
from django.utils import timezone

from shop.models import Comment, ProductDiscount
from orders.models import Order


class PublishCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["is_active"]
        labels = {"is_active": ""}


class OrderPayForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["paid"]
        labels = {"paid": ""}


class DiscountProductForm(forms.ModelForm):

    start_time = forms.DateTimeField(initial=timezone.now)
    discount_percent = forms.IntegerField(max_value=100, min_value=0)

    class Meta:
        model = ProductDiscount
        fields = ["discount_percent", "start_time", "end_time"]
