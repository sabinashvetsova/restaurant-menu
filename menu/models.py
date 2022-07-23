from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Allergen(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    allergens = models.ManyToManyField(Allergen, null=True, blank=True)
    energy_value = models.FloatField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name
