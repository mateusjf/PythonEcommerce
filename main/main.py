from utilitarios.funcoes import *
from dao.Dao import Dao
from Controller.Controller import *
from view.view import *
from padrao.Singleton import *
from padrao.FactoryProduto import *
from padrao.TipoLivro import *
from padrao.TipoTv import *
from padrao.TipoViolao import *

from model.Cliente import *
from model.Livro import *
from model.Tv import *
from model.Violao import *
from model.Pedido import *
from model.Carrinho import *

#from padrao.AbstractProduto import *

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
            print('3 - Historico de Compras')
            print('4 - Verificar Frete Sobre Produto')
            print('5 - Voltar')
            print('')
            try:
                opcao = int(input('Digite uma opcao: '))
                if opcao == 1:
                    self.comprar()
                elif opcao == 2:
                    self.listar_pedidos()
                elif opcao == 3:
                    self.historico_compras()
                elif opcao == 4:
                    self.frete_produto()
                elif opcao == 5:
                    break
                else:
                    continue
            except Exception as e:
                raise e

    def comprar(self):
        SingletonCarrinho.instancia = None
        pedido = Pedido()
        pedido._data_pedido = '26/06/2020'
        pedido.id = len(pedidoDAO.get_lista()) + 1

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

                clearConsole()
                sistemaPagamento = Sistema()
                print('Modo de pagamento: ')
                print('1 - Boleto')
                print('2 - Cartao')

                tipo_pagamento = input('Escolha a forma de pagamento: ')



    def listar_pedidos(self):
        for pedido in pedidoDAO.get_lista():
            pedido.modelo.atualiza_view()

    def historico_compras(self):
        pass

    def frete_produto(self):
        pass

if __name__ == '__main__':
    carregar_base()
    app = Ecommerce()
    app.main()