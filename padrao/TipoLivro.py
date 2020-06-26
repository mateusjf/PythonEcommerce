from padrao import FactoryProduto
from model import Livro

class TipoLivro(FactoryProduto):

    def criar_produto(self):
        return Livro()