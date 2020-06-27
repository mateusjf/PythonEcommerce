from padrao.StrategyFrete import StrategyFrete

class StrategyTv(StrategyFrete):

    def calculaFrete(self, Produto):
        porcentagem = Produto.valor * 0.30
        return porcentagem + Produto._valor