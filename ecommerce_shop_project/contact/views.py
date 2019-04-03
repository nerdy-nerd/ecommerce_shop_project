from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template


def contact(request):
    if request.method == "POST":
        form = ContactForm(data=request.POST)

        if form.is_valid():
            contact_email = form.cleaned_data["contact_email"]

            template = get_template("email.txt")
            context = {
                "contact_name": form.cleaned_data["contact_name"],
                "contact_email": contact_email,
                "form_content": form.cleaned_data["content"],
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website ",
                ["youremail@gmail.com"],
                headers = {"Reply-To": contact_email }
            )
            email.send()
            context_data = {"form": ContactForm()}
            return redirect("contact:contact")
    else:
        context_data = {"form": ContactForm()}

    return render(request, "contact/contact.html", context=context_data)
