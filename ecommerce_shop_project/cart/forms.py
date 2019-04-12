from django import forms


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(max_value=99, min_value=1, label='', initial=1)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
