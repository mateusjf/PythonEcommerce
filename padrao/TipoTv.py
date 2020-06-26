from padrao import FactoryProduto
from model import Tv


class TipoTc(FactoryProduto):

    def criar_produto(self):
        return Tv()