from padrao.AbstractProduto import AbstractProduto

class Tv(AbstractProduto):
    def __init__(self):
        self._marca = "Philco"
        self._polegada = "42.2"
        self._modelo = "Plasma"
        self._id = 2
        self._valor = 1200.99
        self._descricao = "Apenas uma tv"

    def exibir_informacao(self):
        string = 'Tv\n'
        string += 'Id: ' + str(self.id) + '\n'
        string += 'Valor: ' + str(self._valor) + '\n'
        string += 'Descricao: ' + self._descricao + '\n'
        string += 'Marca: ' + self._marca + '\n'
        string += 'Polegada: ' + str(self._polegada) + '\n'
        string += 'Modelo: ' + self._modelo + '\n'
        return string

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, value):
        self._marca = value

    @property
    def pelagada(self):
        return self._polegada

    @pelagada.setter
    def pelagada(self, value):
        self._polegada = value

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, value):
        self._modelo = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value