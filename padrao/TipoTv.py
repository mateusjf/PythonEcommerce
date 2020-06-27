from padrao.FactoryProduto import FactoryProduto
from model.Tv import Tv


class TipoTc(FactoryProduto):

    def criar_produto(self):
        return Tv()