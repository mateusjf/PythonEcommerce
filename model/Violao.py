from padrao import AbstractProduto


class Violao(AbstractProduto):
    def __init__(self):
        self._marca
        self._modelo
        self._cor
        self._entrada_eletrica = False

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, value):
        self._marca = value

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, value):
        self._modelo = value

    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, value):
        self._cor = value

    @property
    def entrada_eletrica(self):
        return self._entrada_eletrica

    @entrada_eletrica.setter
    def entrada_eletrica(self, value):
        self._entrada_eletrica = value


