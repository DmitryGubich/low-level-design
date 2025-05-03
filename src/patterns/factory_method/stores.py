from abc import ABC, abstractmethod

from patterns.factory_method.burger import (
    BurgerType,
    Burger,
    VeganBurger,
    DeluxeVeganBurger,
    CheeseBurger,
    DeluxeCheeseBurger,
)


class BurgerStore(ABC):
    @abstractmethod
    def create_burger(self, item: BurgerType) -> Burger | None:
        pass

    def order_burger(self, type: BurgerType) -> Burger:
        burger = self.create_burger(type)
        print(f"--- Making a {burger.get_name()} ---")
        burger.prepare()
        burger.cook()
        burger.serve()
        return burger


class CheeseBurgerStore(BurgerStore):
    def create_burger(self, item: BurgerType) -> Burger | None:
        if item == BurgerType.CHEESE:
            return CheeseBurger()
        elif item == BurgerType.DELUXECHEESE:
            return DeluxeCheeseBurger()
        else:
            return None


class VeganBurgerStore(BurgerStore):
    def create_burger(self, item: BurgerType) -> Burger | None:
        if item == BurgerType.VEGAN:
            return VeganBurger()
        elif item == BurgerType.DELUXEVEGAN:
            return DeluxeVeganBurger()
        else:
            return None
