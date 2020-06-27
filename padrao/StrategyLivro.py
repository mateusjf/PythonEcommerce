from padrao.StrategyFrete import StrategyFrete

class StrategyLivro(StrategyFrete):

    def calculaFrete(self, Produto):
        porcentagem = Produto.valor * 0.10
        return porcentagem + Produto._valor