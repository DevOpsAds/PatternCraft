from meal_item import MealItem

class Rice(MealItem):
    def description(self):
        return "Arroz"

class Beans(MealItem):
    def description(self):
        return "Feijão"

class Meat(MealItem):
    def description(self):
        return "Carne"