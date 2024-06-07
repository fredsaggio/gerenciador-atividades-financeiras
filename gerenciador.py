#Gerenciador de atividade financeiras
import os.path
import time
from arquivosload import *

def entrada_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, insira apenas números.")

def entrada_int(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, insira apenas números.")

