import datetime 
import calendar
from math import ceil
from gerenciador import *

def init_mes(salario):
    atual = datetime.date.today()
    mes = {"data inicial":atual,"ultimo acesso":0 ,"saldo inicial":0,"semanas":[], "finalizado": False}
    while True:
        print("deseja que o gaf utilize o seu salário como valor inicial para realizar o saldo ou prefere um valor customizado?")
        opc = input("1 - customizado\n2 - automático\n->")
        if opc == '1':
            sal = entrada_float("saldo customizado: ")
            break
        elif opc =='2':
            gasto = entrada_float("gasto total do mês até agora: ")
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
        mes["semanas"].append({"saldo":0,"gasto":0, "extra":0,"ultimo dia":0,"itens":[], "extra_i":[]})
    cont = 0
    for y in range(1, ultimo_dia):#     encontra o último dia da semana
        if calendar.weekday(atual.year,atual.month,y) == 6:
            mes["semanas"][cont]["ultimo dia"] = y
            cont += 1
    mes["semanas"][-1]["ultimo dia"] = ultimo_dia
    for y in range(len(mes["semanas"])):#   procura saber em qual semana estamos
        if atual.day < mes["semanas"][y]["ultimo dia"]:
            semana = y
            mes["ultimo acesso"] = semana
            break
    for y in range(y, len(mes["semanas"])):#    destribui o saldo
        mes["semanas"][y]["saldo"] = sal/(len(mes["semanas"])-semana)
    return mes

def imprimir_mapa(nome, mes, semana):
    gasto = 0
    extra = 0
    saldo_total = 0
    for x in mes["semanas"][semana]["itens"]:
        gasto += x[1]
    for x in mes["semanas"][semana]["extra_i"]:
        extra += x[1]
    saldo_total = mes["semanas"][semana]["saldo"]+extra-gasto
    print(f"Semana {semana+1}:")
    print(f"\tSaldo inicial da semana: {mes["semanas"][semana]["saldo"]:.2f}")
    print(f"\tSaldo total: {saldo_total:.2f}")
    print(f"\tGasto da semana: {gasto:.2f}")
    cont = 0
    for x in mes["semanas"][semana]["itens"]:
        cont += 1
        print(f"\t - gasto {cont}: {x[0]} = R${x[1]:.2f}")
    print(f"\tRenda extra: {extra:.2f}")
    cont = 0
    for x in mes["semanas"][semana]["extra_i"]:
        cont += 1
        print(f"\t - Extra {cont}: {x[0]} = R${x[1]:.2f}")
    if mes["data inicial"].year == datetime.date.today().year and mes["data inicial"].month == datetime.date.today().month:
        if mes["semanas"][semana]["ultimo dia"] == datetime.date.today().day:
            print("Essa semana terminara HOJE!")
        elif mes["semanas"][semana]["ultimo dia"] > datetime.date.today().day:
            print(f"Essa semana terminara no dia {mes["semanas"][semana]["ultimo dia"]} desse mês.")
        else:
            print(f"Essa semana terminou no dia {mes["semanas"][semana]["ultimo dia"]} desse mês.")
    else:
        print(f"Essa semana terminou no dia {mes["semanas"][semana]["ultimo dia"]}/{mes["data inicial"].month}")
    print()

def atualizar_mapa(mes, data_atual=datetime.date.today()):
    aux = ''
    aux2 = ''
    opc = 0
    if data_atual.year == mes["data inicial"].year and mes["data inicial"].month == data_atual.month:
        for y in range(len(mes["semanas"])):#   procura saber em qual semana estamos
            if data_atual.day < mes["semanas"][y]["ultimo dia"]:
                semana_atual = y
                break
        if semana_atual > mes["ultimo acesso"]:
            if semana_atual - mes["ultimo acesso"] > 1:
                aux = 's'
            print(f"Notamos que já faz {semana_atual-mes["ultimo acesso"]} semana{aux} desde o último aceso")
            while opc not in [1,2]:
                print(f"Deseja adicionar algum item dessa{aux} ultima{aux} semana{aux}?\n1 - Sim\n2 - Não")
                opc = entrada_int("->")
                if opc not in [1,2]:
                    print("Por favor, digite apenas \'1\' ou \'2\'!")
            if opc == 1:
                if semana_atual-mes["ultimo acesso"] > 1:
                    for x in range(mes["ultimo acesso"], semana_atual-1):
                        print(f"Semana {x+1}")
                        adicionar_itens(mes, x)
                        clear()
                print(f"Semana {semana_atual}")
                adicionar_itens(mes, semana_atual-1)
                clear()
            saldo_acumulado = 0
            for x in range(semana_atual):
                gasto = 0
                extra = 0
                if mes["semanas"][x]["saldo"] != 0 and mes["semanas"][x]["gasto"] == 0:
                    for y in mes["semanas"][x]["itens"]:
                        gasto += y[1]
                    mes["semanas"][x]["gasto"] = gasto
                    for y in mes["semanas"][x]["extra_i"]:
                        extra += y[1]
                    mes["semanas"][x]["extra"] = extra
                    saldo_acumulado += mes["semanas"][x]["saldo"]-gasto+extra
            mes["semanas"][semana_atual]["saldo"] += saldo_acumulado
            mes["ultimo acesso"] = semana_atual
    elif data_atual.year > mes["data inicial"].year or data_atual.month > mes["data inicial"].month:
        if data_atual.year-mes["data inicial"].year > 1 or data_atual.month-mes["data inicial"].month > 1:
            aux = 's'
            aux2 = 'meses'
        else:
            aux2 = 'mês'
        if data_atual.year == mes["data inicial"].year:
            print(f"Já se passou {data_atual.month-mes["data inicial"].month} {aux2} desde o último acesso, deseja finalizar o mapa mental?")
        else:
            print(f"Já se passou {data_atual.year-mes["data inicial"].year} ano{aux} desde o último acesso, deseja finalizar o mapa mental?")
        print("Obs: caso não finalize deletaremos TODAS as informações do mapa")
        while opc not in [1, 2]:
            opc = entrada_int("1 - sim\n2 - não\n->")
            if opc not in [1, 2]:
                print("Por favor, Digite somente 1 e 2!")
        if opc == 2:
            mes.clear()
        elif opc == 1:
            opc = 0
            while opc not in [1,2]:
                print(f"\nDeseja adicionar algum gasto dessa{aux} ultima{aux} semana{aux}?\n1 - Sim\n2 - Não")
                opc = entrada_int("->")
                if opc not in [1,2]:
                    print("Por favor, digite apenas \'1\' ou \'2\'!")
            if opc == 1:
                clear()
                for x in range(len(mes["semanas"])):
                    if mes["semanas"][x]["saldo"] != 0 and mes["semanas"][x]["gasto"] == 0:
                        print(f"Semana {x+1}")
                        adicionar_itens(mes, x)
                        clear()
            saldo_acumulado = 0
            for x in range(len(mes["semanas"])-1):
                if mes["semanas"][x]["saldo"] != 0 and mes["semanas"][x]["gasto"] == 0:
                    for y in mes["semanas"][x]["itens"]:
                        gasto += y[1]
                    mes["semanas"][x]["gasto"] = gasto
                    for y in mes["semanas"][x]["extra_i"]:
                        extra += y[1]
                    mes["semanas"][x]["extra"] = extra
                    saldo_acumulado += mes["semanas"][x]["saldo"]-gasto+extra
                gasto = 0
                extra = 0
            for y in mes["semanas"][-1]["itens"]:
                gasto += y[1]
            mes["semanas"][-1]["gasto"] = gasto
            for y in mes["semanas"][-1]["extra_i"]:
                extra += y[1]
            mes["semanas"][-1]["extra"] = extra
            saldo_acumulado += mes["semanas"][x]["saldo"]-gasto+extra
            mes["semanas"][-1]["saldo"] = saldo_acumulado
            mes["ultimo acesso"] = len(mes["semanas"])-1
            mes["finalizado"] = True
    else:
        print("Variável inválida")

def adicionar_itens(mes, semana, itens=0):
    while True:
        valor = 0
        nome = input("Digite o nome do item no qual deseja adicionar ou digite \'0\' para sair da função.\n->").strip()
        if nome == '0':
            break
        while valor <= 0:
            valor = entrada_float(f"Digite o valor do item \"{nome}\" em Reais: R$")
            if valor <= 0:
                print("O preço não pode ser negativo nem nulo")
        if itens == 1:
            mes["semanas"][semana]["extra_i"].append([nome,valor])
        else:
            mes["semanas"][semana]["itens"].append([nome,valor])

