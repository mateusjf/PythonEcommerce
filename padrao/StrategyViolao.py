from padrao.StrategyFrete import StrategyFrete

class StrategyViolao(StrategyFrete):

    def calculaFrete(self, Produto):
        porcentagem = Produto.valor * 0.20
        return porcentagem + Produto._valor