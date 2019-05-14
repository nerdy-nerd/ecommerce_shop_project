from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.http import HttpResponseRedirect

from .models import OrderItem
from .forms import OrderCreateForm, AddressCreateForm
from cart.cart import Cart
from .tasks import order_created
from account.models import Address, User


def order_create(request, address_uuid=None):
    cart = Cart(request)
    if request.method == "POST":
        if request.user.is_authenticated:
            form = OrderCreateForm(request.POST, user=request.user)
        elif address_uuid:
            form = OrderCreateForm(request.POST, address_uuid=address_uuid)
        else:
            form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = order.address.user
            order.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    price=item["price"],
                    quantity=item["quantity"],
                )
            cart.clear()
            order_created.delay(order.id)
            return render(request, "orders/order/created.html", {"order": order})
    else:
        if request.user.is_authenticated:
            form = OrderCreateForm(user=request.user)
        elif address_uuid:
            form = OrderCreateForm(address_uuid=address_uuid)
        else:
            form = OrderCreateForm()
    return render(request, "orders/order/create.html", {"form": form})


class AddressCreateView(CreateView):
    model = Address
    template_name = "orders/order/new_address.html"
    form_class = AddressCreateForm

    def get_success_url(self):
        if self.request.user.is_authenticated:
            return reverse_lazy("orders:order_create")
        else:
            return reverse_lazy(
                "orders:order_create", kwargs={"address_uuid": self.object.uuid}
            )

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["logged"] = self.request.user.is_authenticated
        return kwargs

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
            self.object = form.save()

        else:  # If user is anonymous get or create non_active account
            email = form.cleaned_data["email"]
            user = User.objects.filter(email=email).first()
            if not user:
                user = User(email=email, is_active=False)
                user.set_password("pass")
                user.save()
            form.instance.user = user
            form.cleaned_data.pop("email", None)
            # get address if exists, otherwise create
            address = Address.objects.filter(user=user, **form.cleaned_data).first()
            if not address:
                self.object = form.save()
            else:
                self.object = address
        return HttpResponseRedirect(self.get_success_url())

