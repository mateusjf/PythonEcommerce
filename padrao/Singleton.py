from model import Carrinho

class SingletonCarrinho:
    instancia = None

    @staticmethod
    def getInstancia(self):
        if SingletonCarrinho.instancia == None:
            SingletonCarrinho.instancia = Carrinho()

        return SingletonCarrinho.instancia
