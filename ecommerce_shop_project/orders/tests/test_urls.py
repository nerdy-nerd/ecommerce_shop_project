from django.test import SimpleTestCase
from django.urls import resolve, reverse


from ..views import order_create, AddressCreateView

import uuid


class TestUrls(SimpleTestCase):
    def test_create_url_is_resolved(self):
        url = reverse("orders:order_create")
        self.assertEquals(resolve(url).func, order_create)

    def test_create_with_address_url_is_resolved(self):
        url = reverse("orders:order_create", args=[uuid.uuid4()])
        self.assertEquals(resolve(url).func, order_create)

    def test_new_address_url_is_resolved(self):
        url = reverse("orders:new_address")
        self.assertEquals(resolve(url).func.view_class, AddressCreateView)

