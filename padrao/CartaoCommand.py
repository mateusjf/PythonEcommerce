from padrao.Command import Command

class CartaoCommand(Command):

    def __init__(self, objeto):
        self.objeto = objeto

    def execute(self):
        self.objeto.pagar_cartao()