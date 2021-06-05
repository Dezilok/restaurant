from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Food
from ..utils.Mixins import AccessOnlyForStaff


class FoodListView(ListView):
    model = Food


class FoodDetailView(DetailView):
    model = Food


class FoodCreateView(AccessOnlyForStaff, CreateView):
    model = Food
    fields = ['name', 'image', 'price', 'description', 'foodType']


class FoodUpdateView(AccessOnlyForStaff, UpdateView):
    model = Food
    fields = [
        'name',
        'image',
        'price',
        'description',
        'foodType'
    ]
    action = "Update"


