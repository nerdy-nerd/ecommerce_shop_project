from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]


class RatingForm(forms.Form):
    rating = forms.IntegerField(max_value=5, min_value=1)
