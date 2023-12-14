import random
import click
from typing import Callable
from pizza import SIZE, pizza_range, Pizza


def rename(newname):
    """
    Renaming for functions bake, delivery and pickup
    for better understanging in outputs.
    """

    def decorator(f):
        f.__name__ = newname
        return f

    return decorator


def log(func: Callable) -> Callable:
    """
    Decorator for obtaining operation time
    """

    def wrapper(*args, **kwargs):
        action_time = random.randint(2, 30)
        res = func(*args, **kwargs)
        message = f"{func.__name__} - {{}} minutes!"
        print(message.format(action_time))
        return res

    return wrapper


@log
@rename("Your pizza baked in")
def bake(pizza: Pizza):
    """
    Output that pizza is being baked.
    """
    print(
        f"Baking is started ⏰! Info: {pizza.name} with size {pizza.size} ..."
    )


@log
@rename("Your pizza delivered in")
def deliver(pizza: Pizza):
    """
    Output info about delivery.
    """
    print(
        f"Your {pizza.name} size {pizza.size} is ready!\n"
        f"The courier 🚗 is on his way!"
    )


@log
@rename("You picked up the pizza in")
def pickup(pizza: Pizza):
    """
    Output that pizza is ready for pickup.
    """
    print(
        f"Your pizza {pizza.name} size {pizza.size} is ready!\n"
        f"Hot and tasty! Waiting for you!"
    )


@click.group()
def main() -> None:
    pass


@main.command()
@click.option("--delivery", default=False, is_flag=True)
@click.option(
    "--size",
    default="L",
    type=click.Choice([s for s in SIZE], case_sensitive=False),
)
@click.argument("pizza_name", nargs=1)
def order(pizza_name: str, delivery: bool, size: str) -> None:
    """
    Order creation, production and delivery.
    Args:
        pizza_name - pizza title
        delivery - flag for delivery
        size: size of the pizza, L or XL
    Return: none
    """
    pizza_name = pizza_name.lower()
    if pizza_name not in pizza_range:
        print(
            f"Wrong pizza name! Please check, got {pizza_name}, expected one from menu"
        )
    else:
        cur_pizza = pizza_range[pizza_name](size=size)
        bake(cur_pizza)
        if delivery:
            deliver(cur_pizza)
        else:
            pickup(cur_pizza)


@main.command()
def menu() -> None:
    """
    Print menu.
    :return: None
    """
    print("Menu:")
    for ind, pizza in enumerate(pizza_range.values()):
        print(str(ind + 1) + ". ", pizza().description)


if __name__ == "__main__":
    main()
