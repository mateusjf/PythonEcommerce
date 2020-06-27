from model.Livro import *
from model.Violao import *
from model.Tv import *

class Controller:
    def __init__(self, modelo, visao):
        self.visao = visao
        self.modelo = modelo

    def atualiza_view(self):
        self.visao.printDetalhe(self.modelo.exibir_informacao())
