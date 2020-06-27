from model.Livro import *
from model.Violao import *
from model.Tv import *

class Controller:
    def __init__(self, modelo, visao):
        self.visao = visao
        self.modelo = modelo

    def atualiza_view(self):
        self.visao.printDetalhe(self.modelo.exibir_informacao())
"""
    @property
    def visao(self):
        return self._visao

    @visao.setter
    def visao(self, value):
        self._visao = value

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, value):
        self._modelo = value

"""