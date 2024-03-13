from meal_item import MealItem

class Box(MealItem):
    def __init__(self, name):
        super().__init__(name, 0, 0)
        self.children = []



    def description(self,name):
        self.children.append(name)
    
    def add_item(self, item):
        self.children.append(item)

    def remove_item(self, item):
        self.children.remove(item)

    def get_cost(self):
        total_cost = 0
        for child in self.children:
            total_cost += child.get_cost()
        return total_cost

    def get_total_weight(self):
        total_weight = 0
        for child in self.children:
            total_weight += child.get_total_weight()
        return total_weight

    def show_items(self):
        for child in self.children:
            child.show_items()
