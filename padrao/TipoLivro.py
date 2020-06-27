from padrao.FactoryProduto import FactoryProduto
from model.Livro import Livro

class TipoLivro(FactoryProduto):

    def criar_produto(self):
        return Livro()