from rest_framework import serializers

from menu.models import Category, Dish, Allergen


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class AllergenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allergen
        fields = ["name"]


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ["name", "category", "allergens", "energy_value", "price", "image"]
