from padrao import Command

class CartaoCommand(Command):

    def __init__(self, objeto):
        self.objeto = objeto

    def execute(self):
        pass