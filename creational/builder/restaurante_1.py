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

class Rice(MealItem):
    def description(self):
        return "Arroz"

class Beans(MealItem):
    def description(self):
        return "Feijão"

class MealBuilder:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_cost(self):
        total_cost = 0
        for item in self.items:
            total_cost += item.price
        return total_cost

    def get_total_weight(self):
        total_weight = 0
        for item in self.items:
            total_weight += item.weight
        return total_weight / 1000  # Convertendo de gramas para quilogramas

    def show_items(self):
        for item in self.items:
            print(f"Item: {item.name}, Price: {item.price}, Weight: {item.weight}g")

# Exemplo de uso
meal_builder = MealBuilder()
meal_builder.add_item(Rice("Arroz", 5.00, 50))
meal_builder.add_item(Beans("Feijão", 3.00, 100))

print("Detalhes do Pedido:")
meal_builder.show_items()
print(f"Total de Kilogramas na Refeição: {meal_builder.get_total_weight()}kg")
print(f"Custo Total: R$ {meal_builder.get_cost():.2f}")
