from abc import ABC, abstractmethod

class StrategyFrete(ABC):

    @abstractmethod
    def calculaFrete(self, Produto):
        raise NotImplementedError()

