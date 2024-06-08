from gerenciador import *
from arquivosload import *
from mapa_financeiro import *
from financiamento import *

def menu_gerenciador():
    while True:
        lerArquivo('arquivostexto/menu.txt')
        entrada = input('\nEscolha uma das opções acima: ')
        
        if entrada == '1':
            clear()
            print("Preencha com seus dados de acordo com a indicação abaixo.")
            saldo = entrada_float('Digite o saldo: ')
            quantidade = entrada_int("Digite a quantidade de gastos, dívidas ou produtos a se pagar: ")
            produtos = []
            dividas = 0.0
            for i in range(quantidade):
                nome_divida = input(f"Me diga o NOME da dívida/produto {i+1}: ")
                valor_divida = entrada_float(f"qual o VALOR da dívida/produto {i+1}: ")
                dividas += valor_divida
                produtos.append((nome_divida, valor_divida))
            for nome_divida, valor_divida in produtos:
                print(f"Gasto: {nome_divida}, Valor: R$ {valor_divida:.2f}")
            print(f"O saldo restante para gastos é R$ {saldo - dividas:.2f}")
            continuar = entrada_int("Deseja continuar no GAF? 1. sim ou 2. não: ")
            sair_programa = 0
            while True:
                if continuar == 2:
                    clear()
                    print("Obrigado por usar nossa plataforma GAF!\nGAF: O seu amigo das finanças ;)!")
                    sair_programa = 1
                    break
                elif continuar == 1:
                    clear()
                    print("Voltando...")
                    time.sleep(1.25)
                    break
                else:
                    print("Valor inválido")
            if sair_programa == 1:
                break
        #essas funções ainda não estão prontas
        elif entrada == '2':
            print(init_mes(entrada_float("Por favor digite o seu salário!\n->")))
        elif entrada == '3':
            financiamento(entrada_float("Por favor digite o saldo no qual deseja investir: "))
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

