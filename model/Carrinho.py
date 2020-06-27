class Carrinho(object):
    def __init__(self):
        self._id_carrinho = -1
        self.produtos = []

    @property
    def id(self):
        return self._id_carrinho

    @id.setter
    def id(self, value):
        self._id_carrinho = value
        """
    @property
    def Pedido(self):
        return self._Pedido

    @Pedido.setter
    def Pedido(self, value):
        self._Pedido = value
        """