from meal_builder import MealBuilder
from creational.builder.restaurante.classes.meals import Rice,Beans

# Exemplo de uso
meal_builder = MealBuilder()
meal_builder.add_item(Rice("Arroz", 5.00, 50))
meal_builder.add_item(Beans("Feijão", 3.00, 100))

print("Detalhes do Pedido:")
meal_builder.show_items()
print(f"Total de Kilogramas na Refeição: {meal_builder.get_total_weight()}kg")
print(f"Custo Total: R$ {meal_builder.get_cost():.2f}")
print(f"Valor Total dos Itens na Caixa: R$ {meal_builder.get_price():.2f}")