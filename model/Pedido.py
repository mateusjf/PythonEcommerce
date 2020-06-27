class Pedido:

    def __init__(self):
        self._id_pedido = -1
        self._data_pedido = None
        self._Cliente = None
        self._Carrinho = None

        @property
        def id(self):
            return self._data_pedido

        @id.setter
        def id(self, value):
            self._id_pedido = value

        @property
        def data_pedido(self):
            return self._data_pedido

        @data_pedido.setter
        def data_pedido(self, value):
            self._data_pedido = value

        @property
        def Cliente(self):
            return self._Cliente

        @Cliente.setter
        def Cliente(self, value):
            self._Cliente = value

        @property
        def Carrinho(self):
            return self._Carrinho

        @Carrinho.setter
        def Carrinho(self, value):
            self._Carrinho = value

    def __str__(self):
        string = ""
        string += 'Id Pedido: ' + str(self.id) + '\n'
        string += 'Data Pedido: ' + str(self._data_pedido) + '\n'
        return string
