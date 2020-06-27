from abc import ABC, abstractmethod

class StrategyFrete(ABC):

    @abstractmethod
    def calcularFrete(self, Produto):
        raise NotImplementedError()

