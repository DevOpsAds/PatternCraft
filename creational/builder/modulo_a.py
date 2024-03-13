from builder_simple import PersonBuilder
# Exemplo de uso:
builder = PersonBuilder()
builder.set_name("John")
builder.set_age(30)
person = builder.get_result()
print(person)  # Saída: Name: John, Age: 30
