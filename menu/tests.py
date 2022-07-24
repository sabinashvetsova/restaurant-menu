from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from django.test import Client

from menu.models import Dish, Category, Allergen


class DishTests(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username="test",
            email="test@email.com",
            password="test",
        )
        token, _ = Token.objects.get_or_create(user=self.user)
        self.client = Client(HTTP_AUTHORIZATION=f"Token {token.key}")

    def test_create_dish(self):
        url = reverse("dishes")
        Category.objects.create(name="Desserts")
        Allergen.objects.create(name="Eggs")
        data = {
            "name": "Cheese cake",
            "category": 1,
            "allergens": [1],
            "energy_value": 200,
            "price": "5",
            "image": "cheesecake.jpeg",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Dish.objects.count(), 1)
        dish = Dish.objects.get()
        self.assertEqual(dish.name, "Cheese cake")
        self.assertEqual(dish.category.name, "Desserts")
