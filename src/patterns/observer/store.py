from abc import ABC, abstractmethod


class Store(ABC):
    @abstractmethod
    def add_customer(self, customer):
        pass

    @abstractmethod
    def remove_customer(self, customer):
        pass

    @abstractmethod
    def notify_customers(self):
        pass

    @abstractmethod
    def update_quantity(self, quantity):
        pass


class BookStore(Store):
    def __init__(self):
        self._customers = []
        self._stock_quantity = 0

    def add_customer(self, customer):
        self._customers.append(customer)

    def remove_customer(self, customer):
        self._customers.remove(customer)

    def notify_customers(self):
        for customer in self._customers:
            customer.update(self._stock_quantity)

    def update_quantity(self, quantity):
        self._stock_quantity = quantity
        self.notify_customers()


class Customer(ABC):
    @abstractmethod
    def update(self, stock_quantity):
        pass


class BookCustomer(Customer):
    def __init__(self, store):
        self._store = store
        self._observed_stock_quantity = None
        self._store.add_customer(self)

    def update(self, stock_quantity):
        self._observed_stock_quantity = stock_quantity
        if stock_quantity > 0:
            print("Hello, A book you are interested in is back in stock!")
