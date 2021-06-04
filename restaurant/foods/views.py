from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import UserPassesTestMixin

from .models import Food


class FoodListView(ListView):
    model = Food


class FoodDetailView(DetailView):
    model = Food


class FoodCreateView(UserPassesTestMixin, CreateView):
    def test_func(self):
        return self.request.user.is_staff

    model = Food
    fields = ['name', 'image', 'price', 'description', 'foodType']


