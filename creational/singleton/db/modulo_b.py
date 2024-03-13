from my_database import MyDatabaseClassic, User
import modulo_a

# Executar o exemplo de uso do módulo a
modulo_a.run_example()

# Remover usuários "Bob" e "Charlie" adicionados pelo módulo a
database = MyDatabaseClassic.get_instance()
database.remove(1)  # Remover "Bob"
database.remove(1)  # Remover "Charlie"
database.remove(1)  # Remover "Charlie"

# Exemplo de uso do módulo b
user1 = User("Roberto", 25)
database.add(user1)

user2 = User("Jona", 30)
database.add(user2)

user3 = User("Luiza", 35)
database.add(user3)

# Remover usuário pelo índice
database.remove(0)

database.show()
