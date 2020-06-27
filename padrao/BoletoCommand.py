from padrao.CartaoCommand import Command


class BoletoCommand(Command):

    def __init__(self, objeto):
        self.objeto = objeto

    def execute(self):
        self.objeto.pagar_boleto()