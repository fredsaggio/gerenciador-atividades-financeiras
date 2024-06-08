from mapa_financeiro import *
import datetime
import calendar

tempo = datetime.date(2025, 6, 29)
mes = {'data inicial': datetime.date(2029, 6, 8), 'ultimo acesso': 1, 'saldo inicial': 10000.0, 'semanas': [
{'saldo': 0, 'gasto': 0, 'extra': 0, 'ultimo dia': 2, 'itens': [], 'extra_i': []}, 
{'saldo': 2500.0, 'gasto': 0, 'extra': 0, 'ultimo dia': 9, 'itens': [], 'extra_i': []}, 
{'saldo': 2500.0, 'gasto': 0, 'extra': 0, 'ultimo dia': 16, 'itens': [], 'extra_i': []}, 
{'saldo': 2500.0, 'gasto': 0, 'extra': 0, 'ultimo dia': 23, 'itens': [], 'extra_i': []}, 
{'saldo': 2500.0, 'gasto': 0, 'extra': 0, 'ultimo dia': 30, 'itens': [], 'extra_i': []}]}

atualizar_mapa(mes, tempo)
print(mes)

