from padrao.StrategyFrete import StrategyFrete

class StrategyViolao(StrategyFrete):

    def calcularFrete(self, Produto):
        porcentagem = Produto.valor * 0.20
        return porcentagem