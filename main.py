from funcao import *

def main():
    while True:
        clear()
        lerArquivo('arquivostexto/opcoes.txt')
        opcao = input('\nEscolha uma das opções acima: ')

        if not opcao.isnumeric() or int(opcao) not in range(1, 5):
            print('\nvalor inválido')
            time.sleep(1.5)

        # Login
        elif opcao == '1':
            if len(dados_perfil) > 0:
                menu_login()
            else:
                clear()
                print("Não existe nenhum usuário para acessar! Por favor, crie um.")
                time.sleep(2)
                clear()
            
        # Registro
        elif opcao == '2':
            menu_registro(dados_perfil)
            
        elif opcao == '3':
            if len(dados_perfil) > 0:
                excluir_usuario(dados_perfil)
            else:
                clear()
                print("Não existe nenhum usuário para exluir!!")
                time.sleep(2)
                clear()

        # Sair do programa
        else:
            while True:
                clear()

                confirmar = input('Tem certeza que deseja sair do programa? [s/n]: ').strip().lower()

                if confirmar in ['s', 'sim', 'si', 'yes', 'y']:
                    print('Programa finalizado, até a próxima!')
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


main()
