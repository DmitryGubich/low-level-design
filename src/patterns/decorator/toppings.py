from patterns.decorator.beverage import Beverage


class BeverageDecorator(Beverage):
    def __init__(self, beverage):
        self.beverage = beverage


class EspressoDecorator(BeverageDecorator):
    def __init__(self, beverage):
        super().__init__(beverage)

    def cost(self):
        return 0.5 + self.beverage.cost()

    def description(self):
        return self.beverage.description() + ", Espresso"


class CreamDecorator(BeverageDecorator):
    def __init__(self, beverage):
        super().__init__(beverage)

    def cost(self):
        return 0.3 + self.beverage.cost()

    def description(self):
        return self.beverage.description() + ", Cream"


class FoamDecorator(BeverageDecorator):
    def __init__(self, beverage):
        super().__init__(beverage)

    def cost(self):
        return 0.2 + self.beverage.cost()

    def description(self):
        return self.beverage.description() + ", Foam"
