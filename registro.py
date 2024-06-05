import time
from arquivosload import clear, lerArquivo, armazenarDados, carregarDados
from main import contas

while True:
    clear()

    # Registra um novo usuário
    registrar_usuario = input('Digite um nome de usuário para registro: ')

    if registrar_usuario in contas: 
        print('Este nome de usuário já existe.')
        time.sleep(1.25)
        continue

    if len(registrar_usuario) < 5:
        print('Seu nome de usuário deve conter no mínimo 5 caracteres.')
        time.sleep(1.25)
        continue

    # Registra uma nova senha
    registrar_senha = input('Digite uma senha para registro: ')

    if len(registrar_senha) < 5:
        print('Sua senha deve conter no mínimo 5 caracteres.')
        time.sleep(1.25)
        continue

    contas[registrar_usuario] = registrar_senha

    print('Criando conta...')
    armazenarDados('dados/contas.json', contas)
    time.sleep(1.25)

    clear()
    print('Nome de usuário e senha salvos!')
    time.sleep(0.5)
    print('Voltando ao menu principal...')
    time.sleep(1.25)
    break