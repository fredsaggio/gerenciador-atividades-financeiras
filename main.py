from funcao import *


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
            print('Carregando...')
            time.sleep(1.25)
            clear()
            opc = 0
            print("\nBem vindo, ao mapa financeiro\n")
            print("1 - Criar novo mapa")
            print("2 - Carregar um existente")
            print("3 - Sair da função")
            while opc not in [1,2]:
                opc = entrada_int("->")
                if opc not in [1,2]:
                    print("Por favor, digite somente 1 e 2!")
            if opc == 1:
                clear()
                nome = input('Digite seu nome: ')
                mes = init_mes()
                print()
                imprimir_mapa(nome, mes, mes["ultimo acesso"])
                armazenarDados('dados/dados.json', mes)
            elif opc == 2:
                if len(mes) > 0:
                    atualizar_mapa(mes)
                    opc = 0
                    while opc != 4 and mes["finalizado"] == False:
                        clear()
                        print("Semana atual")
                        imprimir_mapa(nome, mes, mes["ultimo acesso"])
                        print("\n1 - Adicionar gasto\n2 - Adicionar renda extra\n3 - Imprimit todas as semanas")
                        print("4 - Sair")
                        opc = 0
                        while opc not in [1,2,3,4]:
                            opc = entrada_int("\n->")
                            if opc not in [1,2,3,4]:
                                print("Por favor, digite somente os 1, 2, 3 ou 4!")
                        if opc == 1:
                            adicionar_itens(mes, mes["ultimo acesso"])
                        elif opc == 2:
                            adicionar_itens(mes, mes["ultimo acesso"], 1)
                        elif opc == 3:
                            clear()
                            for x in range(mes["ultimo acesso"]+1):
                                imprimir_mapa(nome, mes, x)
                            input("Dê enter para voltar...")
                    while opc != 3 and mes["finalizado"] == True:
                        clear()
                        print("Última semana do mapa financeiro")
                        imprimir_mapa(nome, mes, mes["ultimo acesso"])
                        print("\n1 - Imprimir todas as semanas\n2 - Criar arquivo txt do mapa financeiro\n3 - Sair")
                        opc = 0 
                        while opc not in [1,2,3]:
                            opc = entrada_int("->")
                            if opc not in [1,2,3]:
                                print("Por favor, digite somente os números 1, 2 ou 3!")
                        if opc == 1:
                            clear()
                            for x in range(mes["ultimo acesso"]+1):
                                imprimir_mapa(nome, mes, x)
                            input("Dê enter para voltar...")
                        elif opc == 2:
                            clear()
                            imprimir_txt_mapa(mes, nome)
                            time.sleep(1.25)

                    clear()
                else:
                    print("\nNão há mapa financeiro para carregar, por favor inicie uma!\n")
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