from django.views.generic import ListView, DetailView, CreateView

from .models import Food


class FoodListView(ListView):
    model = Food


class FoodDetailView(DetailView):
    model = Food


class FoodCreateView(CreateView):
    model = Food
    fields = ['name', 'image', 'price', 'description', 'foodType']


