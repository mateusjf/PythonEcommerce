class AbstractProduto(object):
    def __init__(self):
        self._valor = 0.0
        self._descricao = ""
        self._id = -1

    @abstractmethod
    def exibir_informacao(self):
        raise NotImplementedError()

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, value):
        self._valor = value

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, value):
        self._descricao = value

    @property
    def id(self):
        return self._id
