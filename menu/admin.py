from django.contrib import admin

from menu.models import Category, Dish


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    pass
