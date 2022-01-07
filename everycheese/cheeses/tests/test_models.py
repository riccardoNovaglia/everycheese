import pytest

from .factories import CheeseFactory

pytestmark = pytest.mark.django_db


def test_str_output():
    cheese = CheeseFactory()
    assert str(cheese) == cheese.name
