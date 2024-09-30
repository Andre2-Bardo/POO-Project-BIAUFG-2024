from pessoaFisica import PessoaFisica
from abc import abstractmethod

class Funcionario(PessoaFisica):
    
    __codAtual = 3000000000
    
    def __init__(self, nome: str, data_de_nascimento: str, endereco: str, telefone: str, email: str, cpf: int,
                cargo: str, carteira_de_trabalho: str, salario: float, duracao: str, expediente: str, beneficios: list, 
                login: str, senha: str, nivel_de_acesso: str):
        super().__init__(nome, data_de_nascimento, endereco, telefone, email, cpf, login, senha, nivel_de_acesso)
        self.__cargo = cargo
        self.__carteira_de_trabalho = carteira_de_trabalho
        self.__salario = salario
        self.__duracao = duracao
        self.__expediente = expediente
        self.__beneficios = beneficios
        self.__pagamento = 0
        
    @classmethod
    def __increment_cod(cls):
        cls.__codAtual += 1
        return cls.__codAtual
        
    #TODO
    def __str__(self):
        pass
    
    def adicionar_bonus(self, bonus: float):
        self.__pagamento += bonus
    
    def adicionar_salario(self):
        self.__pagamento += self.__salario
    
    @property
    def cargo(self):
        return self.__cargo

    @cargo.setter
    def cargo(self, cargo: str):
        self.__cargo = cargo

    @property
    def carteira_de_trabalho(self):
        return self.__carteira_de_trabalho
    
    @carteira_de_trabalho.setter
    def carteira_de_trabalho(self, nova_ct):
        self.__carteira_de_trabalho = nova_ct

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, salario: float):
        self.__salario = salario

    @property
    def duracao(self):
        return self.__duracao
    
    @duracao.setter
    def duracao(self, nova_duracao):
        self.__duracao = nova_duracao

    @property
    def expediente(self):
        return self.__expediente

    @expediente.setter
    def expediente(self, expediente: str):
        self.__expediente = expediente

    @property
    def beneficios(self):
        return self.__beneficios

    @beneficios.setter
    def beneficios(self, beneficios: list):
        self.__beneficios = beneficios

    @property
    def pagamento(self):
        return self.__pagamento
    
    @pagamento.setter
    def pagamento(self, novo_pagamento: float):
        self.__pagamento += self.__salario
        
