from .arquivosload import *
from .investimento import *
from .gerenciador import *
from .mapa_financeiro import *
from os import mkdir

if not os.path.exists("dados"):
    mkdir("dados")
dados_perfil = carregarDados('dados/dados.json')

def menu_registro(dados_perfil):
    while True:
        clear()
        registrar_usuario = input('Digite um nome de usuário para registro: ')

        if registrar_usuario in dados_perfil: 
            print('Este nome de usuário já existe.')
            time.sleep(1.25)
            continue

        if len(registrar_usuario) < 5:
            print('Seu nome de usuário deve conter no mínimo 5 caracteres.')
            time.sleep(1.25)
            continue
        
        print('Criando conta...')
        dados = {registrar_usuario: {}} 
        dados_perfil.update(dados)
        time.sleep(1.25)

        clear()
        print('Perfil criado!')
        armazenarDados('dados/dados.json', dados_perfil)
        time.sleep(0.5)
        print('Voltando ao menu principal...')
        time.sleep(1.25)
        break

def menu_login():
    clear() 
    print('Direcionando ao login...')
    time.sleep(1) 
    
    while True:  
        clear()
        print("Usuários existentes:")
        for x in dados_perfil:
            print(f"\t-{x}")
        print("\nDê enter para sair.")
        usuario = input('Digite seu nome de usuário: ').strip()
        
        # Verifica se o perfil está dentro do dicionário
        if usuario in dados_perfil:
            clear()
            print('Entrando no perfil...')
            time.sleep(1.25)  
            clear()  
            menu_gerenciador(usuario, dados_perfil)  # Chama o menu do GAF
            break
        elif usuario == "":
            break
        else:
            print('Esse perfil não existe.')
            time.sleep(1)  
            clear()  
            while True:
                opcao = input('Deseja tentar novamente? [s/n]').strip().lower()
                if opcao in ['s', 'sim', 'si', 'y', 'yes']:
                    break  
                elif opcao in ['n', 'não', 'no']:
                    print('Voltando ao menu principal...')
                    time.sleep(1.25)  
                    break  
                else:
                    print('Valor inválido.')    
                    time.sleep(1.25)  
                    clear() 
            if opcao == 'n':
                break 

def excluir_usuario(dados_perfil):
    perfil_excluir = 'Salve professor'
    while perfil_excluir != '':
        print('-'*30)
        print('Lista de perfis:')
        for i in dados_perfil:
            print(i)
        print('-'*30)
        print('\nPara sair, aperte "enter"')
        perfil_excluir = input('Qual perfil você deseja excluir? ').strip()

        if perfil_excluir not in dados_perfil:
            print('Esse perfil não existe.')
        else:
            confirmar = input('Tem certeza que deseja excluir esse perfil? [s/n]: ').strip().lower()

            if confirmar in ['s', 'sim', 'si', 'yes', 'y']:
                print('Perfil excluído.')
                dados_perfil.pop(perfil_excluir)
                armazenarDados('dados/dados.json', dados_perfil)
                time.sleep(1.25)
                break

            elif confirmar in ['n', 'não', 'nao', 'no']:
                print('Voltando ao menu principal...')
                time.sleep(1.25)
                break
            else:
                print('Valor inválido.')
                time.sleep(1.25)
            # If pra sair do loop principal
            if confirmar in ['s', 'sim', 'si', 'yes']:
                break
            

def menu_gerenciador(nome, dados_perfil):
    mes = dados_perfil[nome]
    opc = 0
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
                clear()
                nome_divida = input(f"Me diga o NOME da dívida/produto {i+1}: ")
                valor_divida = entrada_float(f"Qual o VALOR da dívida/produto {i+1}: ")
                dividas += valor_divida
                produtos.append((nome_divida, valor_divida))
            clear()
            for nome_divida, valor_divida in produtos:
                print(f"Gasto: {nome_divida}, Valor: R$ {valor_divida:.2f}")
            print(f"O saldo restante para gastos é R$ {saldo - dividas:.2f}")
            continuar = input("Deseja continuar no GAF? [s/n]: ")
            sair_programa = 0
            while True:
                if continuar in ['n', 'não', 'nao', 'no']:
                    clear()
                    print("Obrigado por usar nossa plataforma GAF!\nGAF: O seu amigo das finanças ;)!")
                    sair_programa = 1
                    break
                elif continuar in ['s', 'sim', 'si', 'yes', 'y']:
                    clear()
                    print("Voltando...")
                    time.sleep(1.25)
                    clear()
                    break
                else:
                    print("Valor inválido")
            if sair_programa == 1:
                break
        
        elif entrada == '2':
            clear()
            opc = 0
            print("\nBem vindo ao mapa financeiro\n")
            print("1 - Criar novo mapa")
            print("2 - Carregar um existente")
            print("3 - Sair da função")
            while opc not in [1,2,3]:
                opc = entrada_int("->")
                if opc not in [1,2,3]:
                    print("Por favor, digite somente 1 e 2!")
            if opc == 1:
                clear()
                mes = init_mes()
                print()
                imprimir_mapa(nome, mes, mes["ultimo acesso"])
            elif opc == 2:
                clear()
                if len(mes) > 0:
                    atualizar_mapa(mes)
                    dados_perfil[nome] = mes
                    armazenarDados('dados/dados.json', dados_perfil)
                    opc = 0
                    while opc != 5 and mes["finalizado"] == False:
                        clear()
                        print("Semana atual")
                        imprimir_mapa(nome, mes, mes["ultimo acesso"])
                        print("\n1 - Adicionar gasto\n2 - Adicionar renda extra\n3 - Imprimir todas as semanas")
                        print("4 - Imprimir em arquivo txt\n5 - Sair")
                        opc = 0
                        while opc not in [1,2,3,4,5]:
                            opc = entrada_int("\n->")
                            if opc not in [1,2,3,4,5]:
                                print("Por favor, digite somente os 1, 2, 3, 4 ou 5!")
                        if opc == 1:
                            adicionar_itens(mes, mes["ultimo acesso"])
                        elif opc == 2:
                            adicionar_itens(mes, mes["ultimo acesso"], 1)
                        elif opc == 3:
                            clear()
                            for x in range(mes["ultimo acesso"]+1):
                                imprimir_mapa(nome, mes, x)
                            input("Dê enter para voltar...")
                        elif opc == 4:
                            if not os.path.exists('mapas_financeiros'):
                                mkdir('mapas_financeiros')
                            imprimir_txt_mapa(mes, nome, mes["ultimo acesso"])
                            time.sleep(1.25)
                        dados_perfil[nome] = mes
                        armazenarDados('dados/dados.json', dados_perfil)
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
                            if not os.path.exists("mapa_financeiros"):
                                mkdir("mapas_financeiros")
                            imprimir_txt_mapa(mes, nome, mes["ultimo acesso"])
                            time.sleep(1.25)
                    clear()
                else:
                    clear()
                    print("\nNão há mapa financeiro para carregar, por favor inicie uma!\n")
                    time.sleep(1.5)
            clear()
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
            clear()
            print("Valor inválido.")
            time.sleep(1.25)
            clear()

