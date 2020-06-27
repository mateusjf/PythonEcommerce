from padrao.TextoCareTaker import *
from padrao.TextoMemento import *
class Texto:

    def __init__(self):
        self._texto = ''
        self.caretaker = TextoCareTaker()

    def escrever_texto(self, novo_texto):
        self.caretaker.adicionar_memento(TextoMemento(self._texto))
        self._texto += novo_texto

    def desfazer_escrita(self):
        self._texto = self.caretaker.get_ultimo_estado().get_texto_salvo()

    def mostrar_texto(self):
        print(self._texto)
