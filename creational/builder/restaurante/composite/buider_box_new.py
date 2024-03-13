from composite_box import Box
from creational.builder.restaurante.classes.meals import MealItem, Rice, Beans, Meat

def build_box_from_items(items):
    box = Box("Caixa Principal")
    for item in items:
        box.add_item(item)
    return box

# Função para receber os pratos como entrada
def get_items_from_input():
    items = []
    while True:
        print("Digite o nome do prato (ou 'fim' para terminar):")
        name = input().strip()
        if name.lower() == "fim":
            break
        print("Digite o preço do prato:")
        price = float(input().strip())
        print("Digite o peso do prato:")
        weight = float(input().strip())
        # Criando instâncias de pratos específicos
        item = None
        if name.lower() == "arroz":
            item = Rice(name, price, weight)
        elif name.lower() == "feijão":
            item = Beans(name, price, weight)
        elif name.lower() == "carne":
            item = Meat(name, price, weight)
        else:
            print("Prato não reconhecido. Por favor, insira 'arroz', 'feijão' ou 'carne'.")
            continue
        items.append(item)
    return items

# Recebendo os pratos como entrada
pratos = get_items_from_input()

# Construindo o box com base nos pratos fornecidos
box = build_box_from_items(pratos)

# Exibindo os detalhes do box
print(box.description())
print("Detalhes da Caixa:")
box.show_items()
print(f"Total de Kilogramas na Caixa: {box.get_total_weight()}kg")
print(f"Custo Total: R$ {box.get_cost():.2f}")
