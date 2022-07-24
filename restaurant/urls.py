"""restaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from menu import views
from menu.views import DishApiView

router = routers.DefaultRouter()
router.register(r"categories", views.CategoryViewSet)
router.register(r"allergens", views.AllergenViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
    path("menu/", views.menu_index, name="menu_index"),
    path("order/<str:dish_id>/add", views.add_to_order, name="add_to_order"),
    path(
        "order/<str:dish_id>/remove", views.remove_from_order, name="remove_from_order"
    ),
    path("order/", views.view_an_order, name="order"),
    path("dishes/", DishApiView.as_view(), name="dishes"),
]
