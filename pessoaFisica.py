from pessoa import Pessoa
from abc import abstractmethod

class PessoaFisica(Pessoa):
    def __init__(self, nome: str, data_de_nascimento: str, endereco: str, telefone: str, email: str, cpf: int,
                login: str, senha: str, nivel_de_acesso: str):
        super().__init__(nome, data_de_nascimento, endereco, telefone, email)
        self.__cpf = cpf
        self.__login = login
        self.__senha = senha
        self.__nivel_de_acesso = nivel_de_acesso

    @abstractmethod
    def __str__(self):
        pass

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, novo_cpf):
        self.__cpf = novo_cpf
    
    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, login: str):
        self.__login = login

    def checar_senha(self, senha: str) -> bool:
        return self.__senha == senha

    @property
    def nivel_de_acesso(self):
        return self.__nivel_de_acesso

    @nivel_de_acesso.setter
    def nivel_de_acesso(self, nivel_de_acesso: list):
        self.__nivel_de_acesso = nivel_de_acesso
        