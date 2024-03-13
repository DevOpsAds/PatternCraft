from composite_box import Box
from creational.builder.restaurante.classes.meals import Rice, Beans,Meat



main_box = Box("Caixa Principal")
print(main_box.description())

# Criando itens individuais
rice = Rice("Arroz", 5.00, 50)
beans = Beans("Feijão", 3.00, 100)
meat = Meat("Carne", 26.00, 100)
# Adicionando os itens à caixa principal
main_box.add_item(rice)
main_box.add_item(beans)
main_box.add_item(meat)

# Exibindo os detalhes da caixa principal
print("Detalhes da Caixa Principal:")
main_box.show_items()
print(f"Total de Kilogramas na Caixa Principal: {main_box.get_total_weight()}kg")
print(f"Custo Total: R$ {main_box.get_cost():.2f}")

