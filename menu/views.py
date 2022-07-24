from django.shortcuts import render, redirect
from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from menu.models import Category, Dish, Allergen
from menu.serializers import CategorySerializer, DishSerializer, AllergenSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class AllergenViewSet(viewsets.ModelViewSet):
    queryset = Allergen.objects.all()
    serializer_class = AllergenSerializer
    permission_classes = [permissions.IsAuthenticated]


class DishApiView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, _):
        dishes = Dish.objects.all()
        serializer = DishSerializer(dishes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DishSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def menu_index(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, "menu_index.html", context)


def add_to_order(request, dish_id):
    request.session["order"] = request.session.get("order", {})
    if not request.session["order"].get(dish_id):
        request.session["order"][dish_id] = 1
    else:
        request.session["order"][dish_id] = request.session["order"][dish_id] + 1
    return redirect(request.META["HTTP_REFERER"])


def remove_from_order(request, dish_id):
    request.session["order"] = request.session.get("order", {})
    dish_count = request.session["order"].get(dish_id, 0)
    if dish_count == 1:
        del request.session["order"][dish_id]
    elif dish_count > 1:
        request.session["order"][dish_id] = request.session["order"][dish_id] - 1
    return redirect(request.META["HTTP_REFERER"])


def view_an_order(request):
    order = request.session.get("order")
    dishes = Dish.objects.filter(id__in=order.keys()) if order else []
    for dish in dishes:
        dish.count = order[str(dish.id)]
    price = sum([dish.price * dish.count for dish in dishes])
    context = {
        "dishes": dishes,
        "price": price,
    }
    return render(request, "order.html", context)
