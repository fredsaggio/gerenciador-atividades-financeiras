#Gerenciador de atividade financeiras
import os.path
import time
from arquivosload import *

contas = carregarDados('dados/contas.json')
def menu_gerenciador():

    lerArquivo('arquivostexto/menu.txt')

    while True:
        entrada = input('\nEscolha uma das opções acima: ')
        
        if entrada == '1':
            while True:
                clear()
                print("Preencha com seus dados de acordo com a indicação abaixo.")
                saldo = input('Digite o saldo: ')
                if not saldo.isnumeric():
                        print("Entrada inválida! Digite apenas números.")
                else:
                    saldo_int = int(saldo)
                    break
            while True:
                quantidade = input("Digite a quantidade de gastos, dívidas ou produtos a se pagar: ")
                if not quantidade.isnumeric():
                    print("Entrada inválida! Digite apenas números.")
                else:
                    quantidade_int = int(quantidade)
                    break
            produtos = []
            dividas = 0.0
            for i in range(quantidade_int):
                nome_divida = input(f"Me diga o NOME da dívida/produto {i+1}: ")
                while True:
                    valor_divida = input(f"qual o VALOR da dívida/produto {i+1}: ")
                    if not valor_divida.isnumeric():
                        print("Entrada inválida! Digite apenas números.")
                    else:
                        valor_divida_int = float(valor_divida)
                        break
                dividas += valor_divida_int
                produtos.append((nome_divida, valor_divida_int))
            for nome_divida, valor_divida_int in produtos:
                print(f"Gasto: {nome_divida}, Valor: R$ {valor_divida_int:.2f}")
            print(f"O saldo restante para gastos é R$ {saldo_int - dividas:.2f}")
            while True:
                continuar = input("Deseja continuar no GAF? 1. sim ou 2. não: ")
                try:
                    continuar_int = int(continuar)
                    break
                except ValueError:
                    print("Entrada inválida! Digite apenas números.")
                    continue
            if continuar_int == 2:
                print("Obrigado por usar nossa plataforma GAF!\nGAF: O seu amigo das finanças ;)!")
                break
            else:
                print("Voltando...")
        #essas funções ainda não estão prontas
        elif entrada == '2':
            print("Mapa")
        elif entrada == '3':
            print("Simulações de investimento")
        elif entrada == '4':
            clear()
            print("Obrigado por usar nossa plataforma GAF!\nGAF: O seu amigo das finanças ;")
            time.sleep(1.25)
            clear()
            print('Saindo...')
            time.sleep(1.25)
            break
        else:
            print("Valor inválido.")

menu_gerenciador()