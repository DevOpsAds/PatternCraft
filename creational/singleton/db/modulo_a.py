from my_database import MyDatabaseClassic, User

def run_example():
    # Exemplo de uso:
    database = MyDatabaseClassic.get_instance()

    user1 = User("Alice", 25)
    database.add(user1)

    user2 = User("Bob", 30)
    database.add(user2)

    user3 = User("Charlie", 35)
    database.add(user3)

    user4 = User("Daniel", 35)
    database.add(user4)
    # Remover usuário pelo índice
    # database.remove(0)

    database.show()

if __name__ == "__main__":
    run_example()
