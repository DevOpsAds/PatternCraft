from abc import ABC, abstractmethod

class MealItem(ABC):
    def __init__(self, name, price, weight):
        self._name = name
        self._price = price
        self._weight = weight

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def weight(self):
        return self._weight

    @abstractmethod
    def description(self):
        pass
