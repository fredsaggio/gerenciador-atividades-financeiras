import os.path
import time
import json

# Função para limpar o console
def clear():
    if os.name == 'posix':  
        return os.system('clear')
    elif os.name == 'nt':   
        return os.system('cls')
    else:
        return None

# Função para ler um arquivo de texto
def lerArquivo(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as arquivooo:
        lerArquivo = arquivooo.read()
    return print(lerArquivo)   
    
# Função para carregar os dados de um arquivo JSON
def carregarDados(arquivo):
    try:
        with open(arquivo, "r", encoding='utf-8') as arquivoo:
            dados = json.load(arquivoo)
        return dados
    except FileNotFoundError:
        return {}
    
# Função para armazenar os dados após finalizar o programa
def armazenarDados(arquivo, conteudo):
    with open(arquivo, 'a', encoding='utf-8') as arquivoo:
        json.dump(conteudo, arquivoo)