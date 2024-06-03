#Gerenciador de atividade financeiras
import os.path
import time
from carregartexto import lerArquivo


def main():

    lerArquivo('menu')

    while True:
        entrada = input(f'\nEscolha uma das opções acima: ')
        try:
            funcao = int(entrada)
        except ValueError:
            print("Entrada inválida. Vamos! Digite apenas a opção 1, 2 ou 3.")
            continue
        if funcao == 1:
            print("Boa escolha!",
                "Farei algumas operações para mostrar o saldo restante após pagamentos de contas.",
                "Para isso, preciso de alguns dados. Preencha de acordo com a indicação abaixo. ", sep="\n")
            while True:
                sal = input("Digite seu saldo, capital que será utilizado para as finanças: ")
                try:
                    saldo = float(sal)
                    break
                except ValueError:
                    print("Entrada inválida! Digite apenas números.")
            while True:
                qd = input("Digite a quantidade de gastos, dívidas, produtos... a se pagar: ")
                try:
                    quant = int(qd)
                    break
                except ValueError:
                    print("Entrada inválida! Digite apenas números.")
            produtos = []
            dividas = 0.0
            for i in range(quant):
                nd = input(f"Me diga o NOME da dívida/produto {i+1}: ")
                while True:
                    vd = input(f"qual o VALOR da dívida/produto {i+1}: ")
                    try:
                        valor = float(vd)
                        break
                    except ValueError:
                        print("Entrada inválida! Digite apenas números.")
                dividas += valor
                produtos.append((nd, valor))
            for nd, valor in produtos:
                print(f"Gasto: {nd}, Valor: R$ {valor:.2f}")
            print(f"O saldo restante para gastos é R$ {saldo-dividas:.2f}")
            while True:
                cp = input("Deseja continuar no GAF? 1. sim ou 2. não: ")
                try:
                    c = int(cp)
                    break
                except ValueError:
                    print("Entrada inválida! Digite apenas números.")
                    continue
            if c == 2:
                print("Obrigado por usar nossa plataforma GAF!", "GAF: O seu amigo das finanças ;)!", sep="\n")
                break
            else:
                print("Voltando...")
        #essas funções ainda não estão prontas
        elif funcao == 2:
            print("Mapa")
        elif funcao == 3:
            print("Simulações de investimento")
        elif funcao == 4:
            print("Financiamento")
        else:
            print("Obrigado por usar nossa plataforma GAF!", "GAF: O seu amigo das finanças ;)!", sep="\n")
            break

main()