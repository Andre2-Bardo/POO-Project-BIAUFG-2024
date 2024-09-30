from item_do_pedido import ItemDoPedido

class Pedido:
    def __init__(self, itens: list, remetente: str, destinatario: str, destino: str):
        self.__itens = itens
        self.__validarItens()
        self.__valor_total = self.__calcularValorTotal()
        self.__remetente = remetente
        self.__destinatario = destinatario
        self.__destino = destino

    def __validarItens(self):
        if not all(isinstance(item, ItemDoPedido) for item in self.__itens):
            raise TypeError("Todos os itens devem ser instâncias da classe ItemDoPedido.")

    def __calcularValorTotal(self):
        valor_total = 0  
        for item in self.__itens:
            valor_total += item.item.valor * item.quantidade  
        return valor_total 

    @property
    def itens(self):
        return self.__itens

    @itens.setter
    def itens(self, novos_itens: list):
        self.__itens = novos_itens
        self.__validarItens()
        self.__valor_total = self.__calcularValorTotal()

    @property
    def valor_total(self):
        return self.__valor_total

    @property
    def remetente(self):
        return self.__remetente

    @remetente.setter
    def remetente(self, novo_remetente: str):
        self.__remetente = novo_remetente

    @property
    def destinatario(self):
        return self.__destinatario

    @destinatario.setter
    def destinatario(self, novo_destinatario: str):
        self.__destinatario = novo_destinatario

    @property
    def destino(self):
        return self.__destino

    @destino.setter
    def destino(self, novo_destino: str):
        self.__destino = novo_destino
