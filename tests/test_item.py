import pytest

from src.item import Item


@pytest.fixture
def item1():
    return Item('test', 10, 10)


def test_calculate_total_price(item1):
    assert item1.calculate_total_price() == 100


def test_apply_discount(item1):
    assert item1.apply_discount() == 10.0


def test_instantiate_from_csv():
    p = Item.instantiate_from_csv()
    assert len(p) == 5


def test__str__(item1):
    assert str(item1) == "test"


def test_name(item1):
    assert item1.name == "test"


def test__repr__(item1):
    assert repr(item1) == "Имя: test, цена: 10"


def test_init(item1):
    assert item1.name == "test"


# def test__add__(item2, item1):
#     assert item2.__add__(item1) == 20
#
#
# def test_change_lang(item3):
#     assert item3.change_lang == 'RU'
#     assert item3.change_lang == 'EN'
