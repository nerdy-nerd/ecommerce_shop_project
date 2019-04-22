from django import forms

from shop.models import Comment


class PublishCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["is_active"]
        labels = {"is_active": ""}

