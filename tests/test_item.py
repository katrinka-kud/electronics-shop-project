import pytest

from src.item import Item
from src.phone import Phone, Mixin, Keyboard


@pytest.fixture
def item1():
    return Item('test', 10, 10)


def test_calculate_total_price(item1):
    assert item1.calculate_total_price() == 100


def test_apply_discount(item1):
    item1.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8.0


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test__str__(item1):
    assert str(item1) == "test"


def test_name(item1):
    assert item1.name == "test"


def test__repr__(item1):
    assert repr(item1) == "Имя: test, цена: 10"


def test_init(item1):
    assert item1.name == "test"


@pytest.fixture
def item3():
    return Keyboard('test', 10, 10)


def test_change_lang(item3):
    item3.change_lang()
    assert item3.language == 'RU'
    item3.change_lang()
    assert item3.language == 'EN'


def test_set_language(item3):
    with pytest.raises(AttributeError):
        item3.language = "CH"
