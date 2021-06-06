import pytest
from pytest_django.asserts import (assertContains, assertRedirects)

from django.urls import reverse
from django.contrib.sessions.middleware import SessionMiddleware
from django.test import RequestFactory

from restaurant.users.models import User
from ..models import Food
from ..views import (FoodDetailView, FoodListView, FoodCreateView, FoodUpdateView)
from .factories import FoodFactory, food

pytestmark = pytest.mark.django_db


def test_food_list_view_expanded(rf):
    # Get the request
    request = rf.get(reverse("foods:list"))
    # Use the request to get the response
    response = FoodListView.as_view()(request)
    # Test that the response is valid
    assertContains(response, 'Food List')


def test_food_create_view(rf, admin_user, food):
    # Order some food from the FoodFactory
    # Make a request for our new food
    request = rf.get(reverse("foods:add"))
    # Add an authenticated user
    request.user = admin_user
    # Use the request to get the response
    response = FoodCreateView.as_view()(request)
    # Test that the response is valid
    assert response.status_code == 200


def test_food_list_contains_2_foods(rf):
    # Create a couple foods
    food1 = FoodFactory()
    food2 = FoodFactory()
    # Create a request and then a response for a list of foods
    request = rf.get(reverse('foods:list'))
    response = FoodListView.as_view()(request)
    # Assert that the response contains both food names in the template.
    assertContains(response, food1.name)
    assertContains(response, food2.name)


def test_detail_contains_food_data(rf, food):
    # Make a request for our new food
    url = reverse("foods:detail", kwargs={'slug': food.slug})
    request = rf.get(url)
    # Use the request to get the response
    callable_obj = FoodDetailView.as_view()
    response = callable_obj(request, slug=food.slug)
    # Let's test our Food details!
    assertContains(response, food.name)
    assertContains(response, food.image)
    assertContains(response, food.price)
    assertContains(response, food.description)
    assertContains(response, food.foodType)


def test_food_create_form_valid(rf, admin_user):
    # Submit the food add form
    form_data = {
        "name": "Sweat potato",
        "description": "Sweat sweat potato",
        "foodType": Food.FoodType.MEAL,
        "price": 15
    }
    request = rf.post(reverse("foods:add"), form_data)
    request.user = admin_user
    response = FoodCreateView.as_view()(request)

    # Get the food based on the name
    food = Food.objects.get(name="Sweat potato")

    # Test that the cheese matches our form
    assert food.description == "Sweat sweat potato"
    assert food.foodType == Food.FoodType.MEAL
    assert food.price == 15


def test_food_create_correct_title(rf, admin_user):
    """Page title for FoodCreateView should be Add Food."""
    request = rf.get(reverse('foods:add'))
    request.user = admin_user
    response = FoodCreateView.as_view()(request)
    assertContains(response, 'Add Food')


def test_food_update_view(rf, admin_user, food):
    url = reverse("foods:update", kwargs={'slug': food.slug})
    # Make a request for our new food
    request = rf.get(url)
    # Add an authenticated user
    request.user = admin_user
    # Use the request to get the response
    callable_obj = FoodUpdateView.as_view()
    response = callable_obj(request, slug=food.slug)
    # Test that the response is valid
    assertContains(response, "Update Food")


def test_food_update(rf, admin_user, food):
    """POST request to FoodUpdateView updates food and redirects."""
    # Make a request for our new food
    form_data = {'name': food.name, 'description': 'Something new', 'foodType': food.FoodType, 'price': food.price,
                 'image': food.image.url}
    url = reverse("foods:update", kwargs={'slug': food.slug})
    request = rf.post(url, form_data)
    request.user = admin_user
    callable_obj = FoodUpdateView.as_view()
    response = callable_obj(request, slug=food.slug)

    # # Check that the cheese has been changed
    food.refresh_from_db()
    assert food.description == 'Something new'
