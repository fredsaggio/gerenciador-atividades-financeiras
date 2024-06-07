import datetime 
import calendar
from math import ceil
from gerenciador import entrada_float

def init_mes(salario):
    atual = datetime.date.today()
    mes = {"data inicial":atual,"ultimo acesso":atual ,"saldo inicial":0, "gasto mensal":0,"semanas":[]}
    while True:
        print("deseja que o gaf utilize o seu salário como valor inícial para realizar o saldo ou prefere um valor customizado?")
        opc = input("1 - customizado\n2 - automático\n->")
        if opc == '1':
            sal = entrada_float("saldo customizado:")
            break
        elif opc =='2':
            gasto = entrada_float("gasto total do mês:")
            sal = salario-gasto
            if sal < 0:
                print("Você não pode fazer um planejamento financeiro no negativo!!\nPor favor digite os valores novamente.")
            else:
                break
        else:
            print("opção inválida\n\n")
    mes["saldo inicial"] = sal
    ultimo_dia = calendar.monthrange(atual.year, atual.month)[1]
    for y in range(ceil(ultimo_dia/7)):
        mes["semanas"].append({"saldo":0,"gasto":0,"ultimo dia":0})
    cont = 0
    for y in range(1, ultimo_dia):
        if calendar.weekday(atual.year,atual.month,y) == 6:
            mes["semanas"][cont]["ultimo dia"] = y
            cont += 1
    mes["semanas"][-1]["ultimo dia"] = ultimo_dia
    for y in range(len(mes["semanas"])):
        if atual.day < mes["semanas"][y]["ultimo dia"]:
            semana = y
            break
    for y in range(y, len(mes["semanas"])):
        mes["semanas"][y]["saldo"] = sal/(len(mes["semanas"])-semana)
    return mes

