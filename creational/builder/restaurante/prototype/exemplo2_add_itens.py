from abc import ABC, abstractmethod

# Classe abstrata para protótipos de produtos
class ProductPrototype(ABC):
    @abstractmethod
    def clone(self):
        pass

# Subclasse concreta para um tipo de produto no cardápio
class Pizza(ProductPrototype):
    def __init__(self, flavor, price, size="M",peso="Tonelada"):
        self.flavor = flavor
        self.price = price
        self.size = size  # Novo atributo
        self.peso = peso  # Novo atributo

    def clone(self):
        return Pizza(self.flavor, self.price, self.size, self.peso)

    def __str__(self):
        return f"Pizza de {self.flavor} ({self.size}): R$ {self.price:.2f}=: peso {self.peso}"

# Classe que mantém o cardápio e cria cópias dos produtos
class Menu:
    def __init__(self):
        self.products = {}

    def add_product(self, name, product):
        self.products[name] = product

    def get_product(self, name):
        return self.products.get(name)

# Exemplo de uso
if __name__ == "__main__":
    # Criando o cardápio
    menu = Menu()

    # Adicionando produtos ao cardápio
    menu.add_product("Margherita", Pizza("Margherita", 25.00))
    menu.add_product("Pepperoni", Pizza("Pepperoni", 30.00))
    menu.add_product("Vegetariana", Pizza("Vegetariana", 28.00))

    # Clonando e exibindo produtos do cardápio com novo atributo
    margherita_clone = menu.get_product("Margherita").clone()
    margherita_clone.size = "G"  # Definindo novo atributo
    margherita_clone.peso = "Gramas"  # Definindo novo atributo
    print("Cópia do produto no cardápio:", margherita_clone)

    pepperoni_clone = menu.get_product("Pepperoni").clone()
    pepperoni_clone.size = "P"  # Definindo novo atributo
    print("Cópia do produto no cardápio:", pepperoni_clone)

    vegetariana_clone = menu.get_product("Vegetariana").clone()
    vegetariana_clone.size = "M"  # Definindo novo atributo
    vegetariana_clone.peso = "Kilos"  # Definindo novo atributo
    print("Cópia do produto no cardápio:", vegetariana_clone)
