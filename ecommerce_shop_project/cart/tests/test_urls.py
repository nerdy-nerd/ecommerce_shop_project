from django.test import SimpleTestCase
from django.urls import resolve, reverse

from cart.views import cart_add, cart_remove, cart_detail


class TestUrls(SimpleTestCase):
    def test_cart_add_url_is_resolved(self):
        url = reverse("cart:cart_add", args=[1])
        self.assertEquals(resolve(url).func, cart_add)

    def test_cart_remove_url_is_resolved(self):
        url = reverse("cart:cart_remove", args=[1])
        self.assertEquals(resolve(url).func, cart_remove)

    def test_cart_detail_url_is_resolved(self):
        url = reverse("cart:cart_detail")
        self.assertEquals(resolve(url).func, cart_detail)
