from utilitarios.funcoes import *
from dao.Dao import Dao
from Controller.Controller import *
from view.view import *

from padrao.Singleton import *
from padrao.FactoryProduto import *
from padrao.TipoLivro import *
from padrao.TipoTv import *
from padrao.TipoViolao import *
from padrao.Sistema import *
from padrao.Command import *
from padrao.BoletoCommand import *
from padrao.CartaoCommand import *
from padrao.Acao import *
from padrao.ContextFrete import *
from padrao.StrategyLivro import *
from padrao.StrategyTv import *
from padrao.StrategyViolao import *
from padrao.Texto import *

from model.Cliente import *
from model.Livro import *
from model.Tv import *
from model.Violao import *
from model.Pedido import *
from model.Carrinho import *


clienteDAO = Dao()
produtoDAO = Dao()
pedidoDAO = Dao()

TIPO_VIOLAO = TipoViolao()
TIPO_TV = TipoTc()
TIPO_LIVRO = TipoLivro()


def carregar_base():
    violao = TIPO_VIOLAO.criar_produto()
    tv = TIPO_TV.criar_produto()
    livro = TIPO_LIVRO.criar_produto()

    controler_produto1 = Controller(violao, View())
    controler_produto2 = Controller(tv, View())
    controler_produto3 = Controller(livro, View())

    produtoDAO.adicionar(controler_produto1)
    produtoDAO.adicionar(controler_produto2)
    produtoDAO.adicionar(controler_produto3)

    print(produtoDAO.get_lista())


class Ecommerce:

    def __init__(self):
        pass

    def main(self):
        opcao = -1
        while True:
            clearConsole()
            print('Bem Vindo ao Ecommerce')
            print('Escolha as opcoes abaixo: \n')
            print('1 - Cadastrar Cliente')
            print('2 - Login')
            print('3 - Sair')
            print('')

            try:
                opcao = int(input('Digite sua opcao: '))
                if opcao == 1:
                    self.cadastrar_cliente()
                elif opcao == 2:
                    self.login()
                elif opcao == 3:
                    break
                else:
                    continue
            except Exception as e:
                raise e

    def cadastrar_cliente(self):
        clearConsole()
        print('Cadastro Cliente--\n')
        try:
            cliente = Cliente()
            cliente.nome = input('Digite seu nome: ')
            cliente.id = input('Digite seu cpf: ')
            cliente._data_nascimento = input('Digite sua data de nascimento: ')
            cliente_controller = Controller(cliente, View())
            clienteDAO.adicionar(cliente_controller)
            input('Cliete cadastrado...')
        except Exception as e:
            raise e

    def login(self):
        clearConsole()
        cpf = input('Digite o seu cpf: ')
        cliente_controler = clienteDAO.buscar(cpf)
        if cliente_controler == None:
            input('CPF invalido...')
            return

        input('Login aceito...')
        while True:
            opcao = -1
            clearConsole()
            print('Bem Vindo: ' + cliente_controler.modelo.nome)
            print('')
            print('1 - Comprar')
            print('2 - Listar Pedidos')
            print('3 - Enviar feedback')
            print('4 - Verificar Frete Sobre Produto')
            print('5 - Voltar')
            print('')
            try:
                opcao = int(input('Digite uma opcao: '))
                if opcao == 1:
                    self.comprar(cliente_controler.modelo)
                elif opcao == 2:
                    self.listar_pedidos()
                elif opcao == 3:
                    self.enviar_feedback()
                elif opcao == 4:
                    self.frete_produto(cliente_controler.modelo)
                elif opcao == 5:
                    break
                else:
                    continue
            except Exception as e:
                raise e

    def comprar(self, cliente):
        SingletonCarrinho.instancia = None
        pedido = Pedido()
        pedido._data_pedido = '26/06/2020'
        pedido.id = len(pedidoDAO.get_lista()) + 1
        pedido.Cliente = cliente

        controlerPedido = Controller(pedido, View())
        while True:
            clearConsole()

            print('Lista de Produtos')
            for produto in produtoDAO.get_lista():
                produto.atualiza_view()

            carrinho = SingletonCarrinho.getInstancia()
            pedido.Carrinho = carrinho
            id_produto = input('Digite o id do produto ou -1 para sair: ')

            if id_produto == '1':
                c = Controller(TIPO_VIOLAO.criar_produto(), View())
                carrinho.produtos.append(c)
            elif id_produto == '2':
                c = Controller(TIPO_TV.criar_produto(), View())
                carrinho.produtos.append(c)
            elif id_produto == '3':
                c = Controller(TIPO_LIVRO.criar_produto(), View())
                carrinho.produtos.append(c)
            elif id_produto == '-1':
                pedidoDAO.adicionar(controlerPedido)

                while True:
                    clearConsole()
                    print('Modo de pagamento: ')
                    print('1 - Boleto')
                    print('2 - Cartao')

                    comando = None
                    tipo_pagamento = input('Escolha a forma de pagamento: ')
                    if tipo_pagamento == '1':
                        comando = BoletoCommand(Acao())
                        break
                    elif tipo_pagamento == '2':
                        comando = CartaoCommand(Acao())
                        break
                    else:
                        continue
                sistemaPagamento = Sistema()
                sistemaPagamento.processar_pedido(comando)
                input('Compra Finalizada...')

                return

    def listar_pedidos(self):
        for pedido in pedidoDAO.get_lista():
            print(pedido.modelo)

    def enviar_feedback(self):
        memento = Texto()
        while True:
            clearConsole()
            print('Feedback escrito: \n')
            memento.mostrar_texto()

            print('\n1 - Adicionar texto')
            print('2 - Desfazer ultima escrita')
            print('3 - Sair')
            print('')
            opcao = input('Digite sua opcao: ')

            if opcao == '1':
                novo_texto = input('Digite seu texto: ')
                memento.escrever_texto(novo_texto)
            elif opcao == '2':
                memento.desfazer_escrita()
            elif opcao == '3':
                break
            else:
                continue;

    def frete_produto(self, cliente):
        historico = []
        for pedido in pedidoDAO.get_lista():
            if pedido.modelo.Cliente is cliente:
                historico.append(pedido)

        for i in range(len(historico)):
            print(str(i) +  ' - ' + historico[i].modelo.__str__())

        id = int(input('Deseja ver o frete dos produtos de quais pedidos: '))
        meu_historico = historico[id].modelo.Carrinho.produtos
        meus_produtos = []

        for p in meu_historico:
            meus_produtos.append(p.modelo)

        clearConsole()
        for item in meus_produtos:
            if type(item) == Violao:
                contexto = ContextFrete(StrategyViolao())

                print('Marca: ' + item.marca)
                print('Modelo: ' + item.modelo)
                print('Valor Compra: ' + str(item._valor))
                print('Frete: ' + str(contexto.calcularFrete(item)))
                print('')
            elif type(item) == Livro:
                contexto = ContextFrete(StrategyLivro())

                print('Titulo: ' + item.titulo)
                print('Autor: ' + item.autor)
                print('Valor Compra: ' + str(item._valor))
                print('Frete: ' + str(contexto.calcularFrete(item)))
                print('')
            elif type(item) == Tv:
                contexto = ContextFrete(StrategyViolao())

                print('Marca: ' + item.marca)
                print('Modelo: ' + item.modelo)
                print('Valor Compra: ' + str(item._valor))
                print('Frete: ' + str(contexto.calcularFrete(item)))
                print('')

        input('Continuar...')


if __name__ == '__main__':
    carregar_base()
    app = Ecommerce()
    app.main()
