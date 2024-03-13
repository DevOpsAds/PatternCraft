from creational.interfaces.person_inter import User

class MyDatabaseClassic:
    _instance = None

    def __init__(self):
        self.users = []

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def add(self, user):
        self.users.append(user)

    def remove(self, index):
        if 0 <= index < len(self.users):
            del self.users[index]
        else:
            print("Erro: Índice inválido.")

    def show(self):
        for user in self.users:
            print(user)
