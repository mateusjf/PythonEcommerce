class ContextFrete():
    def __init__(self, estrategia):
        self._estrategia = estrategia

    def calcularFrete(self, objeto):
        return self._estrategia.calcularFrete(objeto)