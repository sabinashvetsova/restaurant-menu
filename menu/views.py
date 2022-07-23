from rest_framework import viewsets
from rest_framework import permissions

from menu.models import Category, Dish, Allergen
from menu.serializers import CategorySerializer, DishSerializer, AllergenSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [permissions.IsAuthenticated]


class AllergenViewSet(viewsets.ModelViewSet):
    queryset = Allergen.objects.all()
    serializer_class = AllergenSerializer
    permission_classes = [permissions.IsAuthenticated]
