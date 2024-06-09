from mapa_financeiro import *
import datetime
import calendar

tempo = datetime.date(2025, 6, 29)
mes = init_mes(9000)
atualizar_mapa(mes, tempo)
imprimir_mapa("Carlos", mes, mes["ultimo acesso"])
print(mes)

