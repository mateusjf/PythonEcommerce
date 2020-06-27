from padrao.StrategyFrete import StrategyFrete

class StrategyTv(StrategyFrete):

    def calcularFrete(self, Produto):
        porcentagem = Produto.valor * 0.30
        return porcentagem