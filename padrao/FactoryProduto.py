from abc import ABC, abstractmethod

class FactoryProduto(ABC):

    @abstractmethod
    def criar_produto(self):
        raise NotImplementedError