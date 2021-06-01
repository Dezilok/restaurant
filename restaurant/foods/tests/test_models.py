import pytest

from ..models import Food
from .factories import FoodFactory

pytestmark = pytest.mark.django_db


def test___str__():
    food = FoodFactory()
    assert food.__str__() == food.name
    assert str(food) == food.name

