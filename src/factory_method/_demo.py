from burgertype import BurgerType
from stores import CheeseBurgerStore, VeganBurgerStore

if __name__ == "__main__":
    cheese_store = CheeseBurgerStore()
    vegan_store = VeganBurgerStore()

    burger = cheese_store.order_burger(BurgerType.CHEESE)
    print(f"Ethan ordered a {burger.get_name()}")
    burger = vegan_store.order_burger(BurgerType.VEGAN)
    print(f"Joel ordered a {burger.get_name()}")
