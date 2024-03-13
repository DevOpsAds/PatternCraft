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

# Exemplo de uso
def main():
    # Criando uma caixa
    box = Box("Caixa Principal")

    # Criando um novo item em tempo de execução
    class NewMenuItem(MealItem):
        def description(self):
            return "Novo Item de Menu"

    new_item = NewMenuItem("Macarrão", 10.00, 200)
    new_item1 = NewMenuItem("Arroz", 15.00, 200)
    
    # Adicionando o novo item à caixa
    box.add_item(new_item)
    box.add_item(new_item1)

    # Exibindo os itens na caixa
    box.show_items()

if __name__ == "__main__":
    main()
