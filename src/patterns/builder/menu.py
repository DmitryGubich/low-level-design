from abc import ABC, abstractmethod

from patterns.builder.meal import Meal
from patterns.builder.type import Drink, Starter, Main, Dessert


class Builder(ABC):
    @abstractmethod
    def add_starter(self):
        pass

    @abstractmethod
    def add_main_course(self):
        pass

    @abstractmethod
    def add_dessert(self):
        pass

    @abstractmethod
    def add_drink(self):
        pass


class VeganMealBuilder(Builder):
    def __init__(self):
        self.meal = Meal()

    def add_starter(self) -> Builder:
        self.meal.starter = Starter.SALAD
        return self

    def add_main_course(self) -> Builder:
        self.meal.main = Main.VEGGIE_STIR_FRY
        return self

    def add_dessert(self) -> Builder:
        self.meal.dessert = Dessert.VEGAN_PUDDING
        return self

    def add_drink(self) -> Builder:
        self.meal.drink = Drink.VEGAN_SHAKE
        return self

    def build(self) -> Meal:
        return self.meal


class HealthyMealBuilder(Builder):
    def __init__(self):
        self.meal = Meal()

    def add_starter(self) -> Builder:
        self.meal.starter = Starter.SALAD
        return self

    def add_main_course(self) -> Builder:
        self.meal.main = Main.GRILLED_CHICKEN
        return self

    def add_dessert(self) -> Builder:
        self.meal.dessert = Dessert.FRUIT_SALAD
        return self

    def add_drink(self) -> Builder:
        self.meal.drink = Drink.WATER
        return self

    def build(self) -> Meal:
        return self.meal
