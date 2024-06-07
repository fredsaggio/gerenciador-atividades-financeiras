salario = 3000

def init_mes(salario):
    mes = {"saldo inicial":0, "gasto total":0,"semana 1":[],"semana 2":[],"semana 3":[],"semana 4":[]}
    sal = 0
    gasto = 0
    while True:
        print("deseja que o gaf utilize o seu salário como valor inícial para realizar o saldo ou prefere um valor customizado?")
        opc = input("1 - customizado\n2 - automático\n->")
        if opc == '1':
            sal = float(input("saldo customizado:"))
            break
        elif opc =='2':
            gasto = float(input("gasto total do mês:"))
            sal = salario-gasto
            if sal < 0:
                print("Você não pode fazer um planejamento financeiro no negativo!!\nPor favor digite os valores novamente.")
            else:
                break
        else:
            print("opção inválida\n\n")
    cont = 0
    for x in mes:
        if cont == 0:
            cont += 1
            mes[x] = sal
            continue
        elif cont == 1:
            cont += 1
            continue
        mes[x].append(sal/4)
    return mes

print(init_mes(400))

