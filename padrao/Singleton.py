from model.Carrinho import *

class SingletonCarrinho:
    instancia = None

    @staticmethod
    def getInstancia():
        if SingletonCarrinho.instancia == None:
            SingletonCarrinho.instancia = Carrinho()

        return SingletonCarrinho.instancia
