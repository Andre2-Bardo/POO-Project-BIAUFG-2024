from pessoaFisica import PessoaFisica

class Cliente(PessoaFisica):
    
    def __init__(self, nome: str, data_de_nascimento: str, endereco: str, telefone: str, email: str, cpf: int, 
                login: str, senha: str, nivel_de_acesso: str):
        super().__init__(nome, data_de_nascimento, endereco, telefone, email, cpf, login, senha, nivel_de_acesso)

    #TODO
    def comprar(self):
        pass
    
    #TODO
    def trocar(self):
        pass
