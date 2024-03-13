class MyDatabaseClassic:
    _instance = None

    def __init__(self):
        # Lança um erro se alguém tentar criar uma instância diretamente
        if self._instance is not None:
            raise RuntimeError("Erro: Use MyDatabaseClassic.getInstance() para obter uma instância única.")
    
    @classmethod
    def get_instance(cls):
        # Cria uma instância se ainda não existir
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance


# Exemplo de uso:
db1 = MyDatabaseClassic.get_instance()
db2 = MyDatabaseClassic.get_instance()

print(db1 is db2)  # True, pois db1 e db2 referem-se à mesma instância de MyDatabaseClassic
