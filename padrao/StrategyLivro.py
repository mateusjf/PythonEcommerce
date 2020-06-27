from padrao.StrategyFrete import StrategyFrete

class StrategyLivro(StrategyFrete):

    def calcularFrete(self, Produto):
        porcentagem = Produto.valor * 0.10
        return porcentagem