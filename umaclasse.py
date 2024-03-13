from abc import ABC, abstractmethod

class DocumentosInterface(ABC):
    @abstractmethod
    def get_cpf(self):
        pass

    @abstractmethod
    def get_rg(self):
        pass

class Documentos(DocumentosInterface):
    def __init__(self, cpf, rg):
        self.cpf = cpf
        self.rg = rg

    def get_cpf(self):
        return self.cpf

    def get_rg(self):
        return self.rg

class PessoaInterface(ABC):
    @abstractmethod
    def get_nome(self):
        pass

    @abstractmethod
    def get_sobrenome(self):
        pass

    @abstractmethod
    def get_idade(self):
        pass

class Pessoa(PessoaInterface):
    def __init__(self, nome, sobrenome, idade, documentos):
        self.__nome = nome  # atributo privado
        self.sobrenome = sobrenome  # atributo público
        self._idade = idade  # atributo protegido
        self.documentos = documentos  # atributo público

    def get_nome(self):
        return self.__nome

    def get_sobrenome(self):
        return self.sobrenome

    def get_idade(self):
        return self._idade

# Exemplo de uso:
documentos_pessoa = Documentos("123a45678900", "1234567")
pessoa = Pessoa("João", "Silva", 30, documentos_pessoa)
print("Nome:", pessoa.get_nome())  
print("Sobrenome:", pessoa.get_sobrenome())  
print("Idade:", pessoa.get_idade())  
print("CPF:", pessoa.documentos.get_cpf())  
print("RG:", pessoa.documentos.get_rg())  
