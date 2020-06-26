from padrao import FactoryProduto
from model import Violao


class TipoLivro(FactoryProduto):

    def criar_produto(self):
        return Violao()