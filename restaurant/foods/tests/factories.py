import pytest

from django.template.defaultfilters import slugify

import factory
import factory.fuzzy

from ..models import Food


class FoodFactory(factory.django.DjangoModelFactory):
    name = factory.fuzzy.FuzzyText()
    description = factory.Faker('paragraph', nb_sentences=3, variable_nb_sentences=True)
    foodType = factory.fuzzy.FuzzyChoice([x[0] for x in Food.FoodType.choices])
    slug = factory.LazyAttribute(lambda obj: slugify(obj.name))
    price = factory.fuzzy.FuzzyDecimal(1, 100, 2)

    class Meta:
        model = Food


@pytest.fixture
def food():
    return FoodFactory()
