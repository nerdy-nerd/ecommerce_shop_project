from django import forms


class SubscriptionForm(forms.Form):
    contact_email = forms.EmailField(label="What's your e-mail address?", required=True)

