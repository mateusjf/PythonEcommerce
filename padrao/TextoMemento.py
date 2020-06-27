class TextoMemento:
    def __init__(self, texto):
        self._estado_texto = texto

    def get_texto_salvo(self):
        return self._estado_texto
