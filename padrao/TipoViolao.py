from padrao.FactoryProduto import FactoryProduto
from model.Violao import Violao


class TipoViolao(FactoryProduto):

    def criar_produto(self):
        return Violao()