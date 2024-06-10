from .gerenciador import *

def financiamento(saldo, dias_uteis=252, cdi=0.1195):
    taxa_poupanca = 0.005 * 12
    taxa_atual = 0
    tempo = 0
    cdb = 0
    print("Escolha qual rendimento irá investir.\n1 - CDB\n2 - Poupança")
    while True:
        opcao = entrada_int("\n-> ")
        if opcao == 1:
            taxa_s = "CDB"
            while cdb < 100:
                cdb = entrada_float("Digite o porcentagem de rendimento CDI: ")
                if cdb < 100:
                    print("O valor mínimo do CDB é 100%")
            taxa_atual = cdi * (cdb / 100)
            break
        elif opcao == 2:
            taxa_atual = taxa_poupanca
            taxa_s = "taxa de poupança"
            break
        else:
            print("Valor inválido")

    while tempo < 1:
        print("O tempo que irá investir vai ser em mês ou ano?\n1 - mês\n2 - ano")
        opcao_tempo = entrada_int("-> ")
        if opcao_tempo == 1:
            while tempo < 1:
                tempo = entrada_int("Digite quantos meses pretende investir: ")
                if tempo < 1:
                    print(f"Não existe {tempo} meses")
            if tempo == 1:
                mes_ano = "mês"
            elif tempo > 1:
                mes_ano = "meses"
            break
        elif opcao_tempo == 2:
            while tempo < 1:
                tempo = entrada_float("Digite quantos anos pretende investir: ")
                if tempo < 1:
                    print(f"Para melhor funcionamento do programa digite {round(tempo*12)} meses")
                    break
            if tempo == 1:
                mes_ano = "ano"
            elif tempo > 1:
                mes_ano = "anos"
            break
        else:
            print("Valor inválido! Escolha 1 ou 2!")
    tempo_a = tempo
    if opcao_tempo == 1:
        tempo /= 12


    montante = saldo * ((1 + taxa_atual / dias_uteis) ** (dias_uteis * tempo))
    rendimento_bruto = montante - saldo

    print(f"O seu rendimento bruto do investimento a {taxa_s} em {tempo_a} {mes_ano} é R${rendimento_bruto:.2f} e o montante R${montante:.2f}")

