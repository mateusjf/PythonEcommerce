from padrao import  AbstractProduto

class Livro(AbstractProduto):
    def __init__(self):
        self._autor
        self._paginas
        self._titulo

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, value):
        self._autor = value

    @property
    def paginas(self):
        return self._paginas

    @paginas.setter
    def paginas(self, value):
        self._paginas = value

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, value):
        self._titulo = value