from patterns.decorator.beverage import LightRoast
from patterns.decorator.toppings import FoamDecorator, CreamDecorator, EspressoDecorator

if __name__ == "__main__":
    # fmt: off
    beverage = FoamDecorator(
        CreamDecorator(
            EspressoDecorator(
                LightRoast()
            )
        )
    )
    # fmt: on
    print(beverage.description())  # Output: Light Roast, Espresso, Cream, Foam
    print(beverage.cost())  # Output: 4.45
