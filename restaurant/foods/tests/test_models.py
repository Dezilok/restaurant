import pytest

from ..models import Food
from .factories import FoodFactory

pytestmark = pytest.mark.django_db


def test___str__():
    food = FoodFactory()
    assert food.__str__() == food.name
    assert str(food) == food.name


def test_get_absolute_url():
    food = FoodFactory()
    url = food.get_absolute_url()
    assert url == f'/foods/{food.slug}/'

