from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    price=item["price"],
                    quantity=item["quantity"],
                )
            cart.clear()
            if request.user.is_authenticated:
                request.user.orders.add(order)

        return render(request, "orders/order/created.html", {"order": order})
    else:
        if request.user.is_authenticated:
            data = {
                "first_name": request.user.first_name,
                "last_name": request.user.last_name,
                "email": request.user.email,
                "address": request.user.street,
                "postal_code": request.user.code,
                "city": request.user.city,
                "country": request.user.country,
            }
            form = OrderCreateForm(initial=data)
        else:
            form = OrderCreateForm()
    return render(request, "orders/order/create.html", {"form": form})

