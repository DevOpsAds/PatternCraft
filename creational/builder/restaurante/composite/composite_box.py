from meal_item import MealItem

class Box:
    def __init__(self, name):
        self.name = name
        self.items = []

    def description(self):
        return f"This is {self.name}"

    def add_item(self, item):
        self.items.append(item)

    def show_items(self):
        print(f"Itens da Caixa {self.name}:")
        for item in self.items:
            print(f" - {item.name}: {item.weight}kg - R$ {item.price:.2f}")

    def get_total_weight(self):
        total_weight = sum(item.weight for item in self.items)
        return total_weight

    def get_cost(self):
        total_cost = sum(item.price for item in self.items)
        return total_cost