from django.db import models

from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel


class Food(TimeStampedModel):
    class FoodType(models.TextChoices):
        MEAL = "meal", "Meal"
        DESSERT = "dessert", "Dessert"
        DRINK = "drink", "Drink"

    name = models.CharField("Name of food", max_length=60)
    image = models.ImageField("Image of food", upload_to='images/food/')
    price = models.DecimalField("Price of food", max_digits=8, decimal_places=2)
    slug = AutoSlugField("Food Address", unique=True, always_update=False, populate_from="name")
    description = models.TextField("Description", blank=True)
    foodType = models.CharField("Type of food", max_length=20, choices=FoodType.choices)

    def __str__(self):
        return self.name
