from django import forms

from shop.models import Comment
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
