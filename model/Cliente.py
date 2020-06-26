class Cliente(object):
    def __init__(self):
        self._nome = ""
        self._cpf = ""
        self._data_nascimento = ""
        #self._pedido = None

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, value):
        self._cpf = value
"""
    @property
    def Pedido(self):
        return self._pedido

    @Pedido.setter
    def Pedido(self, value):
        return self._pedido
"""