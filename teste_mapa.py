from funcao import *
import datetime
import calendar

tempo = datetime.date(2024, 6, 16)
mes = init_mes()
atualizar_mapa(mes, tempo)

dados_perfil.update({"Teste":mes})
armazenarDados('dados/dados.json', dados_perfil)
print(mes)

