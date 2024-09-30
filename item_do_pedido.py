from produto import Produto

class ItemDoPedido:
    def __init__(self, item: Produto, quantidade: int):
        self.__item = item
        self.__quantidade = quantidade

    @property
    def item(self):
        return self.__item

    @item.setter
    def item(self, item: Produto):
        self.__item = item

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade: int):
        if quantidade < 0:
            raise ValueError("A quantidade não pode ser negativa.")
        self.__quantidade = quantidade
