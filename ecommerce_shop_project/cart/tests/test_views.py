from django.test import TestCase, Client, RequestFactory
from django.urls import reverse

from cart.cart import Cart
from shop.models import Product, Category


class TestCartDetailView(TestCase):
    def setUp(self):
        self.url = reverse("cart:cart_detail")

    def test_empty_cart(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "Your cart is empty.")
        self.assertEqual(len(response.context["cart"]), 0)

    def test_cart_with_product(self):
        category1 = Category.objects.create(name="category1")
        product1 = Product.objects.create(
            name="product1", original_price=100, category=category1, stock=1
        )
        response = self.client.get(self.url)
        response.context["cart"].add(product=product1)

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "item")
        self.assertEqual(len(response.context["cart"]), 1)

    def test_cart_with_few_products(self):
        category1 = Category.objects.create(name="category1")
        product1 = Product.objects.create(
            name="product1", original_price=100, category=category1, stock=1
        )
        product2 = Product.objects.create(
            name="product2", original_price=100, category=category1, stock=10
        )
        response = self.client.get(self.url)
        response.context["cart"].add(product=product1)
        response.context["cart"].add(product=product2)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["cart"]), 2)


class TestCartAddView(TestCase):
    def setUp(self):
        self.category = category1 = Category.objects.create(name="category1")
        self.product = product1 = Product.objects.create(
            name="product1", original_price=100, category=category1, stock=10
        )

    def test_add_product(self):
        response = self.client.post(reverse("cart:cart_add", args=[self.product.id]))

        self.assertRedirects(
            response,
            reverse("cart:cart_detail"),
            status_code=302,
            target_status_code=200,
        )

    def test_add_product_with_wrong_id(self):
        response = self.client.post(reverse("cart:cart_add", args=[999]))

        self.assertEqual(response.status_code, 404)


class TestCartRemoveView(TestCase):
    def setUp(self):
        self.category = category1 = Category.objects.create(name="category1")
        self.product = product1 = Product.objects.create(
            name="product1", original_price=100, category=category1, stock=10
        )

    def test_remove_product(self):
        response = self.client.post(reverse("cart:cart_remove", args=[self.product.id]))

        self.assertRedirects(
            response,
            reverse("cart:cart_detail"),
            status_code=302,
            target_status_code=200,
        )
        

    def test_remove_product_with_wrong_id(self):
        response = self.client.post(reverse("cart:cart_add", args=[999]))
        self.assertEqual(response.status_code, 404)