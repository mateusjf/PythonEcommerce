from utilitarios.funcoes import *
from dao.Dao import Dao
from Controller.Controller import *
from view.view import *
from model.Cliente import *

clienteDAO = Dao()


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
                elif opcao == 3
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
        pass

    def listar_pedidos(self):
        pass

    def historico_compras(self):
        pass

    def frete_produto(self):
        pass

if __name__ == '__main__':
    app = Ecommerce()
    app.main()