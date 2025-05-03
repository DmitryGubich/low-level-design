from enum import Enum


class Starter(Enum):
    SALAD = 1
    SOUP = 2
    BRUSCHETTA = 3
    VEGGIE_STICKS = 4
    CHICKEN_WINGS = 5


class Main(Enum):
    GRILLED_CHICKEN = 1
    PASTA = 2
    VEGGIE_STIR_FRY = 3
    FISH = 4
    PIZZA = 5


class Dessert(Enum):
    FRUIT_SALAD = 1
    ICE_CREAM = 2
    CHOCOLATE_CAKE = 3
    VEGAN_PUDDING = 4
    CHEESECAKE = 5


class Drink(Enum):
    WATER = 1
    VEGAN_SHAKE = 2
    SODA = 3
    FRUIT_JUICE = 4
