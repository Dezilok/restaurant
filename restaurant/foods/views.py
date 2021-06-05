from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Food
from ..utils.viewmixins import AccessOnlyForStaffMixin


class FoodListView(ListView):
    model = Food


class FoodDetailView(DetailView):
    model = Food


class FoodCreateView(AccessOnlyForStaffMixin, CreateView):
    model = Food
    fields = ['name', 'image', 'price', 'description', 'foodType']


class FoodUpdateView(AccessOnlyForStaffMixin, UpdateView):
    model = Food
    fields = [
        'name',
        'image',
        'price',
        'description',
        'foodType'
    ]
    action = "Update"


