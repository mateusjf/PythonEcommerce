from padrao.TextoMemento import *

class TextoCareTaker:
    def __init__(self):
        self._estados = []

    def adicionar_memento(self, memento):
        self._estados.append(memento)

    def get_ultimo_estado(self):
        if len(self._estados) <= 0:
            return TextoMemento('')
        estado_salvo = self._estados[len(self._estados) - 1]
        self._estados.pop()
        return estado_salvo