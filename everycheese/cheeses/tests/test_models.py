import pytest

pytestmark = pytest.mark.django_db

from ..models import Cheese


def test_str_output():
    cheese = Cheese.objects.create(
        name="Cheddar",
        description="not important",
        firmness=Cheese.Firmness.UNSPECIFIED,
    )
    assert str(cheese) == "Cheddar"
