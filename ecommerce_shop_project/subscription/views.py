from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail, BadHeaderError
from .forms import SubscriptionForm
from django.shortcuts import redirect


def subscription(request):
    if request.method == "POST":
        form = SubscriptionForm(data=request.POST)

        if form.is_valid():
            contact_email = form.cleaned_data["contact_email"]
            context = {"contact_email": contact_email}

            context_data = {"form": SubscriptionForm()}
            try:
                send_mail(
                    "Subscription",
                    "Thank you for subscribing our newsletter. "
                    "This is notification only email. Please do not reply on this email.",
                    ["admin@example.com"],
                    context,
                )
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("subscription:success")
    else:
        context_data = {"form": SubscriptionForm()}

    return render(request, "subscription/subscription.html", context=context_data)


def success_view(request):
    return render(request, "subscription/success.html")

