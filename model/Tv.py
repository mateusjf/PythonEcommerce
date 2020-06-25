from padrao import AbstractProduto

class Tv(AbstractProduto):
    def __init__(self):
        self._marca
        self._polegada
        self._modelo

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, value):
        self._marca = value

    @@property
    def pelagada(self):
        return self._polegada

    @pelagada.setter
    def pelagada(self, value):
        self._polegada = value

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, value):
        self._modelo = value