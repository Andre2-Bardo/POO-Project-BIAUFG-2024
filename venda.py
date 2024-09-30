from pedido import Pedido

class Venda():
    def __init__(self, idPedido: int, dataVenda: str, valorTotal: float, formaPagamento: str, pedido: Pedido):
        self.__idPedido = idPedido
        self.__dataVenda = dataVenda
        self.__valorTotal = valorTotal
        self.__formaPagamento = formaPagamento
        self.__pedido = pedido

    @property
    def valorTotal(self):
        return f'R${round(self.__valorTotal, 2)}'
    
    @valorTotal.setter
    def valorTotal(self, novo_valor):
        self.__valorTotal = novo_valor

    @property
    def registroVenda(self):
        return self