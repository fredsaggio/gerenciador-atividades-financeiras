import datetime
import calendar
from os.path import exists
from math import ceil
from .gerenciador import *

def init_mes():
    atual = datetime.date.today()
    sal = 0
    mes = {"data inicial":[atual.day, atual.month, atual.year],"ultimo acesso":0 ,"saldo inicial":0,"semanas":[], "finalizado": False}
    print("Quanto é o saldo que sera distribuido durante o mês no mapa financeiro?")
    while sal <= 0:
        sal = entrada_float("->")
        if sal <= 0:
            print("O saldo inicial não pode ser negativo!")
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
    data = datetime.date(mes["data inicial"][2],mes["data inicial"][1],mes["data inicial"][0])
    atual = datetime.date.today()
    gasto = 0
    extra = 0
    saldo_total = 0
    for x in mes["semanas"][semana]["itens"]:
        gasto += x[1]
    for x in mes["semanas"][semana]["extra_i"]:
        extra += x[1]
    saldo_total = mes["semanas"][semana]["saldo"]+extra-gasto
    print(f"Semana {semana+1}:")
    print(f"\tSaldo inicial da semana: R${mes["semanas"][semana]["saldo"]:.2f}")
    print(f"\tSaldo total: R${saldo_total:.2f}")
    print(f"\tGasto da semana: R${gasto:.2f}")
    cont = 0
    for x in mes["semanas"][semana]["itens"]:
        cont += 1
        print(f"\t - gasto {cont}: {x[0]} = R${x[1]:.2f}")
    print(f"\tRenda extra: R${extra:.2f}")
    cont = 0
    for x in mes["semanas"][semana]["extra_i"]:
        cont += 1
        print(f"\t - Extra {cont}: {x[0]} = R${x[1]:.2f}")
    if data.year == atual.year and data.month == atual.month:
        if mes["semanas"][semana]["ultimo dia"] == atual.day:
            print("Essa semana terminara HOJE!")
        elif mes["semanas"][semana]["ultimo dia"] > atual.day:
            print(f"Essa semana terminara no dia {mes["semanas"][semana]["ultimo dia"]} desse mês.")
        else:
            print(f"Essa semana terminou no dia {mes["semanas"][semana]["ultimo dia"]} desse mês.")
    else:
        print(f"Essa semana terminou no dia {mes["semanas"][semana]["ultimo dia"]}/{data.month}")
    print()

def imprimir_txt_mapa(mes, nome, semana):
    with open("Mapa financeiro.txt", "w") as file:
        file.write("")
    with open("Mapa financeiro.txt", "a") as file:
        gasto_t = 0
        extra_t = 0
        saldo_total_m = 0
        data = datetime.date(mes["data inicial"][2],mes["data inicial"][1],mes["data inicial"][0])
        data_atual = datetime.date.today()
        for x in range(semana+1):
            for y in mes["semanas"][x]["itens"]:
                gasto_t += y[1]
            for y in mes["semanas"][x]["extra_i"]:
                extra_t += y[1]
        saldo_total_m = mes["saldo inicial"]+extra_t-gasto_t
        file.writelines(f"Mapa financeiro de {nome} iniciado em {data.day}/{data.month}/{data.year}\n")
        file.writelines(f"\nSaldo inicial do mês: R${mes["saldo inicial"]:.2f}\n")
        file.writelines(f"Saldo total do mês: R${saldo_total_m:.2f}\n")
        file.writelines(f"Gasto total do mês: R${gasto_t:.2f}\n")
        file.writelines(f"Renda extra total do mês: {extra_t:.2f}\n")
        file.writelines(f"\nSemanas do dia 1/{data.month} á {mes["semanas"][semana]["ultimo dia"]}/{data.month}\n\n")
        for x in range(semana+1):
            gasto = 0
            extra = 0
            saldo_total = 0
            for y in mes["semanas"][x]["itens"]:
                gasto += y[1]
            for y in mes["semanas"][x]["extra_i"]:
                extra += y[1]
            saldo_total = mes["semanas"][x]["saldo"]+extra-gasto
            if x == 0:
                file.writelines(f"semana 1/{data.month} - {mes["semanas"][x]["ultimo dia"]}/{data.month}:\n")
            else:
                file.writelines(f"semana {mes["semanas"][x-1]["ultimo dia"]}/{data.month} - {mes["semanas"][x]["ultimo dia"]}/{data.month}:\n")
            file.writelines(f"\tSaldo inicial da semana: R${mes["semanas"][x]["saldo"]:.2f}\n")
            file.writelines(f"\tSaldo total: R${saldo_total:.2f}\n")
            file.writelines(f"\tGasto da semana: R${gasto:.2f}\n")
            cont = 0
            for y in mes["semanas"][x]["itens"]:
                cont += 1 
                file.writelines(f"\t - Gasto {cont}: {y[0]} = R${y[1]:.2f}\n")
            file.writelines(f"\tRenda extra: R${extra:.2f}\n")
            cont = 0
            for y in mes["semanas"][x]["extra_i"]:
                cont += 1 
                file.writelines(f"\t - Extra {cont}: {y[0]} = R${y[1]:.2f}\n")
            file.writelines("\n")
        file.writelines(f"Arquivo txt criado no dia {data_atual.day}/{data_atual.month}/{data_atual.year}")
    print("arquivo \"Mapa financeiro.txt\" criado com secesso!")

def atualizar_mapa(mes, data_atual=datetime.date.today()):
    data = datetime.date(mes["data inicial"][2],mes["data inicial"][1],mes["data inicial"][0])
    aux = ''
    aux2 = ''
    opc = 0
    if data_atual.year == data.year and data.month == data_atual.month:
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
    elif (data_atual.year > data.year or data_atual.month > data.month) and mes["finalizado"] == False:
        if data_atual.year-data.year > 1 or data_atual.month-data.month > 1:
            aux = 's'
            aux2 = 'meses'
        else:
            aux2 = 'mês'
        if data_atual.year == data.year:
            print(f"Já se passou {data_atual.month-data.month} {aux2} desde o último acesso, deseja finalizar o mapa mental?")
        else:
            print(f"Já se passou {data_atual.year-data.year} ano{aux} desde o último acesso, deseja finalizar o mapa mental?")
        print("Obs: caso não finalize deletaremos TODAS as informações do mapa serão perdidas!")
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
            mes["semanas"][-1]["saldo"] += saldo_acumulado
            mes["ultimo acesso"] = len(mes["semanas"])-1
            mes["finalizado"] = True
    elif mes["finalizado"] == True:
        print("Mapa financeiro Finalizada")
    else:
        print("Variável inválida")

def adicionar_itens(mes, semana, itens=0):
    while True:
        valor = 0
        nome = input("\nDigite o nome do item no qual deseja adicionar.\n Para sair da função deixe a linha em branco e aperte enter.\n->").strip()
        if nome == '':
            break
        while valor <= 0:
            valor = entrada_float(f"Digite o valor do item \"{nome}\" em Reais: R$")
            if valor <= 0:
                print("O preço não pode ser negativo nem nulo")
        if itens == 1:
            mes["semanas"][semana]["extra_i"].append([nome,valor])
        else:
            mes["semanas"][semana]["itens"].append([nome,valor])

