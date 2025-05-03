class Meal:
    def __init__(self):
        self._starter = None
        self._main = None
        self._dessert = None
        self._drink = None

    @property
    def starter(self):
        return self._starter

    @property
    def main(self):
        return self._main

    @property
    def dessert(self):
        return self._dessert

    @property
    def drink(self):
        return self._drink

    @starter.setter
    def starter(self, starter):
        self._starter = starter

    @main.setter
    def main(self, main):
        self._main = main

    @dessert.setter
    def dessert(self, dessert):
        self._dessert = dessert

    @drink.setter
    def drink(self, drink):
        self._drink = drink
