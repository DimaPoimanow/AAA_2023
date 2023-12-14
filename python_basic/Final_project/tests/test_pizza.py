import pytest

from pizza import Margarita, Pepperoni, Hawaiian, Pizza


class CustomTestPizza(Pizza):
    def __init__(self, size: str = "L") -> None:
        super().__init__(size)
        self.icon = "🥒"
    @property
    def ingredients(self):
        return ['potato', 'carrot']


class AnotherCustomTestPizza(Pizza):
    def __init__(self, size: str = "L") -> None:
        super().__init__(size)
        self.icon = "⚽"
    @property
    def ingredients(self):
        return ['milk', 'orange']


def test_size():
    assert CustomTestPizza().size == 'L'
    assert CustomTestPizza(size='L').size == 'L'
    assert CustomTestPizza(size='XL').size == 'XL'


def test_dict():
    print(f"{CustomTestPizza().dict}")
    # assert TestPizza().dict == [
    #     'Make dough',
    #     'Add a',
    #     'Add b',
    #     'Add c',
    #     'Bake in oven for 20 min'
    # ]


def test_description():
    print(CustomTestPizza().description)
    # assert str(TestPizza()) == 'TestPizza emoji: a, b, c'


def test_base_class_eq():
    assert CustomTestPizza() == CustomTestPizza()
    assert not (CustomTestPizza() == AnotherCustomTestPizza())
    assert not (CustomTestPizza() == CustomTestPizza(size='XL'))


@pytest.mark.parametrize(
    'pizza_class,name,ingredients,icon',
    [
        (
            Margarita, 'Margarita',
            ['tomato sauce', 'mozzarella', 'tomatoes'], '🍅'
        ),
        (
            Pepperoni, 'Pepperoni',
            ['tomato sauce', 'mozzarella', 'pepperoni'], '🍕'
        ),
        (
            Hawaiian, 'Hawaiian',
            ['tomato sauce', 'mozzarella', 'chicken', 'pineapples'], '🍍'
        ),
    ]
)
def test_pizza_class(pizza_class, name, ingredients, icon):
    pizza = pizza_class()
    assert pizza.name == name
    assert pizza.ingredients == ingredients
    assert pizza.icon == icon