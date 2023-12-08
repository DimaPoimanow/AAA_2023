from abc import abstractmethod, ABC
from typing import List, Dict

SIZE = set(["L", "XL"])


class Pizza(ABC):
    """
    Base class for pizza.
    """

    def __init__(self, size: str = "L") -> None:
        super().__init__()
        self.name = self.__class__.__name__
        self.size = size

    @property
    @abstractmethod
    def ingredients(self) -> List[str]:
        """
        List with pizza ingredients.
        """

    def __eq__(self, other_pizza) -> bool:
        """
        Comparing for two pizza (class Pizza) on equality.
        """
        return (self.size == other_pizza.size) and (
            self.ingredients == other_pizza.ingredients
        )

    def dict(self) -> Dict[int, str]:
        """
        Recipe of the pizza in the dict
        Return: dict
        """
        return {
            "1.": "Prepare the dough, roll it into a flat circle.",
            "2.": f"Add ingridients: {', '.join(self.ingredients)}",
            "3.": "Bake for 15 min. That's all",
        }

    @property
    def description(self):
        """
        Get description line from the menu
        Return: str of description
        """
        return f"{self.name} {self.icon} : {', '.join(self.ingredients)}"


class Margarita(Pizza):
    """
    Pizza Margarita
    """

    def __init__(self, size: str = "L") -> None:
        super().__init__(size)
        self.icon = "🍅"

    @property
    def ingredients(self) -> List[str]:
        """
        List with pizza ingredients.
        """
        return ["tomato sauce", "mozzarella", "tomatoes"]


class Pepperoni(Pizza):
    """
    Pizza Pepperoni
    """

    def __init__(self, size: str = "L") -> None:
        super().__init__(size)
        self.icon = "🍕"

    @property
    def ingredients(self) -> List[str]:
        """
        List with pizza ingredients.
        """
        return ["tomato sauce", "mozzarella", "pepperoni"]


class Hawaiian(Pizza):
    """
    Pizza Hawaiian
    """

    def __init__(self, size: str = "L") -> None:
        super().__init__(size)
        self.icon = "🍍"

    @property
    def ingredients(self) -> List[str]:
        """
        List with pizza ingredients.
        """
        return ["tomato sauce", "mozzarella", "chicken", "pineapples"]


pizza_range = {
    "margarita": Margarita,
    "pepperoni": Pepperoni,
    "hawaiian": Hawaiian,
}
