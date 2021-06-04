import pytest

from django.urls import reverse, resolve

from .factories import FoodFactory

pytestmark = pytest.mark.django_db


@pytest.fixture
def food():
    return FoodFactory()


def test_list_reverse():
    """foods:list should reverse to /foods/."""
    assert reverse('foods:list') == '/foods/'


def test_list_resolve():
    """/foods/ should resolve to Foods:list."""
    assert resolve('/foods/').view_name == 'Foods:list'


def test_add_reverse():
    """foods:add should reverse to /foods/add/."""
    assert reverse('foods:add') == '/foods/add/'


def test_add_resolve():
    """/foods/add/ should resolve to Foods:add."""
    assert resolve('/foods/add/').view_name == 'Foods:add'


def test_detail_reverse(food):
    """foods:detail should reverse to /foods/foodslug/."""
    url = reverse('foods:detail', kwargs={'slug': food.slug})
    assert url == f'/foods/{food.slug}/'


def test_detail_resolve(food):
    """/foods/foodslug/ should resolve to Foods:detail."""
    url = f'/foods/{food.slug}/'
    assert resolve(url).view_name == 'Foods:detail'
