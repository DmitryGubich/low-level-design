from abc import ABC, abstractmethod


class Beverage(ABC):
    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def description(self):
        pass


class DarkRoast(Beverage):
    def cost(self):
        return 3.45

    def description(self):
        return "Dark Roast"


class LightRoast(Beverage):
    def cost(self):
        return 3.45

    def description(self):
        return "Light Roast"
