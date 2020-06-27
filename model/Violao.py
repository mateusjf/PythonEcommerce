from padrao.AbstractProduto import AbstractProduto


class Violao(AbstractProduto):
    def __init__(self):
        self._marca = "Fender"
        self._modelo = "M2045"
        self._cor = "Preta"
        self._entrada_eletrica = True
        self._id = 1
        self._valor = 450.50
        self._descricao = "Um violao com entrada eletrica"

    def exibir_informacao(self):
        string = 'Violao\n'
        string += 'Id: ' + str(self._id) + '\n'
        string += 'Valor: ' + str(self._valor) + '\n'
        string += 'Descricao: ' + self._descricao + '\n'
        string += 'Marca: ' + self._marca + '\n'
        string += 'Cor: ' + self._cor + '\n'
        string += 'Modelo: ' + self._modelo + '\n'
        string += 'Eletrica: ' + str(self._entrada_eletrica) + '\n'
        return string

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, value):
        self._marca = value

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, value):
        self._modelo = value

    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, value):
        self._cor = value

    @property
    def entrada_eletrica(self):
        return self._entrada_eletrica

    @entrada_eletrica.setter
    def entrada_eletrica(self, value):
        self._entrada_eletrica = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value


