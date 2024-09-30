from abc import ABC, abstractmethod

class Pessoa(ABC):
    
    __codAtual = 1000000000
    
    def __init__(self, nome: str, data_de_nascimento: str, endereco: str, telefone: str, email: str):
        self.__nome = nome
        self.__data_de_nascimento = data_de_nascimento
        self.__endereco = endereco
        self.__telefone = telefone
        self.__email = email
        self.__codPessoal = Pessoa.__increment_cod()
        
    @classmethod
    def __increment_cod(cls):
        cls.__codAtual += 1
        return cls.__codAtual
        
    @abstractmethod
    def __str__(self):
        pass
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome: str):
        self.__nome = novo_nome

    @property
    def data_de_nascimento(self):
        return self.__data_de_nascimento
    
    @data_de_nascimento.setter
    def data_de_nascimento(self, nova_data: str):
        self.__data_de_nascimento = nova_data

    @property
    def endereco(self):
        return self.__endereco
    
    @endereco.setter
    def endereco(self, novo_endereco: str):
        self.__endereco = novo_endereco

    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, novo_telefone: str):
        self.__telefone = novo_telefone

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, novo_email: str):
        if "@" not in novo_email:
            raise ValueError("Email inválido.")
        self.__email = novo_email

    @property
    def codPessoal(self):
        return self.__codPessoal
    