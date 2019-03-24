from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import AccountRegisterForm


def register(request):
    if request.method == "POST":
        form = AccountRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created")
            return redirect('shop:product_list')

    else:
        form = AccountRegisterForm()
    return render(request, 'account/register.html', {'form': form})
