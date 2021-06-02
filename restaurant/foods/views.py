from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Food


class FoodListView(ListView):
    model = Food


class FoodDetailView(DetailView):
    model = Food


class FoodCreateView(CreateView):
    model = Food
    fields = ['name', 'image', 'price', 'description', 'foodType']
    permission_required = 'food.can_add_food'

