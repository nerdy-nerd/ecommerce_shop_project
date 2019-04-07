from django.shortcuts import render
from .forms import SubscriptionForm
from django.shortcuts import redirect


def subscription(request):
    if request.method == "POST":
        form = SubscriptionForm(data=request.POST)

        if form.is_valid():
            contact_email = form.cleaned_data["contact_email"]
            context = {
                "contact_email": contact_email
            }

            context_data = {"form": SubscriptionForm()}
            return redirect("subscription:subscription")
    else:
        context_data = {"form": SubscriptionForm()}

    return render(request, "subscription/subscription.html", context=context_data)
