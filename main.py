from gerenciador import *
from arquivosload import *
from mapa_financeiro import *
from financiamento import *

def menu_gerenciador():
    mes = {}
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
            opc = 0
            print("Bem vindo, ao mapa financeiro")
            print("1 - Criar novo mapa")
            print("2 - Carregar um existente")
            print("3 - Sair da função")
            while opc not in [1,2]:
                opc = entrada_int("->")
                if opc not in [1,2]:
                    print("Por favor, digite somente 1 e 2!")
            if opc == 1:
                mes = init_mes(5000)
                print(mes)
            elif opc == 2:
                atualizar_mapa(mes)
                print(mes)
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

