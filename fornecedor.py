from pessoa import Pessoa

class Fornecedor(Pessoa):
    
    __codAtual = 2000000000
    
    def __init__(self, nome: str, data_de_nascimento: str, endereco: str, telefone: str, email: str, nome_fantasia: str, cnpj: int):
        super().__init__(nome, data_de_nascimento, endereco, telefone, email)
        self.__nome_fantasia = nome_fantasia
        self.__cnpj = cnpj
        
    @classmethod
    def __increment_cod(cls):
        cls.__codAtual += 1
        return cls.__codAtual
        
    @property
    def nome_fantasia(self):
        return self.__nome_fantasia
        
    @nome_fantasia.setter
    def nome_fantasia(self, novo_nome_fantasia):
        self.__nome_fantasia = novo_nome_fantasia
            
    @property
    def cnpj(self):
        return self.__cnpj
        
    @cnpj.setter
    def cnpj(self, novo_cnpj):
        self.__cnpj = novo_cnpj
            
