from django.test import TestCase
from django.urls import resolve, reverse

from cart.views import cart_add, cart_remove, cart_detail
from cart.forms import CartAddProductForm


class TestForms(TestCase):
    def test_add_cart_form_valid_data(self):
        form = CartAddProductForm(data={"quantity": 2, "update": True})

        self.assertTrue(form.is_valid())

    def test_add_cart_form_invalid_data(self):
        form = CartAddProductForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
