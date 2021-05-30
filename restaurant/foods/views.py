from django.views.generic import ListView, DetailView

from .models import Food


class FoodListView(ListView):
    model = Food
