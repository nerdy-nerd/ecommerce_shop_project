from django import forms
from .models import Order
from account.models import Address


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["address"]

    def __init__(self, *args, address_uuid=None, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if address_uuid:
            self.fields["address"].queryset = Address.objects.filter(uuid=address_uuid)
        elif user:
            self.fields["address"].queryset = Address.objects.filter(user=user)

    address = forms.ModelChoiceField(
        queryset=Address.objects.none(), widget=forms.RadioSelect, empty_label=None
    )


class AddressCreateForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            "name",
            "phone",
            "street",
            "city",
            "province",
            "postal_code",
            "country",
        ]

    def __init__(self, *args, **kwargs):
        logged = kwargs.pop("logged", None)
        super().__init__(*args, **kwargs)
        # If user is anonymous add email field
        if not logged:
            self.fields["email"] = forms.EmailField()
