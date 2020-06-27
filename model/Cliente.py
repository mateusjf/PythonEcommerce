class Cliente:
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
    def id(self):
        return self._cpf

    @id.setter
    def id(self, value):
        self._cpf = value