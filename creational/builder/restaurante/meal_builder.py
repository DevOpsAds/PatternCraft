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

    def get_price(self):
        return sum(item.price for item in self.items)

    def show_items(self):
        for item in self.items:
            print(f"Item: {item.name}, Price: {item.price}, Weight: {item.weight}g")