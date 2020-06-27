from padrao.AbstractProduto import  *

class Livro(AbstractProduto):
    def __init__(self):
        self._autor = "José Aquino"
        self._paginas = "37"
        self._titulo = "A volta dos que nao foram"
        self._id = 3
        self._valor = 88.00
        self._descricao = "Um livro qualquer"

    def exibir_informacao(self):
        string = 'Livro\n'
        string += 'Id: ' + str(self.id) + '\n'
        string += 'Valor: ' + str(self._valor) + '\n'
        string += 'Descricao: ' + self._descricao + '\n'
        string += 'Titulo: ' + self._titulo + '\n'
        string += 'Autor: ' + self._autor + '\n'
        string += 'Paginas: ' + str(self._paginas) + '\n'
        return string

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

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value