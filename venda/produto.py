from pessoa.fornecedor import Fornecedor

class Produto:
    def __init__(self, marca: str, tamanho: str, genero: str, valor: float, tipo: str, fornecedor: Fornecedor):
        self.__marca = marca
        self.__tamanho = tamanho
        self.__genero = genero
        self.__valor = valor
        self.__tipo = tipo
        self.__fornecedor = fornecedor

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca: str):
        self.__marca = marca

    @property
    def tamanho(self):
        return self.__tamanho

    @tamanho.setter
    def tamanho(self, tamanho: str):
        self.__tamanho = tamanho

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, genero: str):
        self.__genero = genero

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor: float):
        self.__valor = valor

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo: str):
        self.__tipo = tipo
        
    @property
    def fornecedor(self):
        return self.__fornecedor
    
    @fornecedor.setter
    def fornecedor(self, novo_fornecedor: Fornecedor):
        self.__fornecedor = novo_fornecedor
