# Giovanne Silveira Henrique - RGM: 47808667
# Algoritmo 2 ATM - Simulador de ATM.
# =================================================

from datetime import datetime

estoque = {100: 10, 50: 10, 20: 10, 10: 10}

def ler_quantidade_abastecimento(mensagem):
   
    entrada = input(mensagem)
    if entrada == "":
        return 0
    try:
        return int(entrada)
    except ValueError:
        print("Valor inválido! Nenhuma nota adicionada.")
        return 0

while True:

    hoje = datetime.now().strftime("%d/%m/%Y")
    
    print("UNICSUL - Simulador de Meio de Pagamento - versão 2026" ,hoje, sep="        ")

    print(
'''    
Menu
Escolha um operação: 
0 - Mostrar quantidade de notas disponíveis de cada valor
1 - Abastecer ATM com quantidade de notas para cada valor
2 - Sacar dinheiro no ATM 
9 - Sair
''')
  
    try:
        opcao = int(input("Escolha uma operação: "))
    except ValueError:
        print("Opção Inválida! Digite um número.")
        continue

    if opcao == 0:
        print("===================NOTAS DISPONÍVEIS=========================")
        print(f"Notas 10: {estoque[10]}")
        print(f"Notas 20: {estoque[20]}")
        print(f"Notas 50: {estoque[50]}")
        print(f"Notas 100: {estoque[100]}")
        print("=============================================================")

    elif opcao == 1:

        estoque[10] += ler_quantidade_abastecimento("Notas 10: ")
        estoque[20] += ler_quantidade_abastecimento("Notas 20: ")
        estoque[50] += ler_quantidade_abastecimento("Notas 50: ")
        estoque[100] += ler_quantidade_abastecimento("Notas 100: ")
        print("Abastecimento concluído.")

    elif opcao == 2:
        try:
            valor = int(input("Valor do saque: "))
        except ValueError:
            print("Valor inválido!")
            continue

        if valor % 10 != 0:
            print("O valor do saque deve ser múltiplo de 10.")
            continue

        valor_restante = valor
        notas_separadas_para_saque = {100: 0, 50: 0, 20: 0, 10: 0}

        for nota in [100, 50, 20, 10]:
            qtd_necessaria = valor_restante // nota
            qtd_disponivel = estoque[nota]
            
            qtd_sacada = min(qtd_necessaria, qtd_disponivel)
            
            notas_separadas_para_saque[nota] = qtd_sacada
            valor_restante -= qtd_sacada * nota

        if valor_restante == 0:
            for nota in [100, 50, 20, 10]:
                estoque[nota] -= notas_separadas_para_saque[nota]

            print("\nSaque realizado com sucesso")
            print(f"Valor: {valor}")
            print(f"Notas 10: {notas_separadas_para_saque[10]}")
            print(f"Notas 20: {notas_separadas_para_saque[20]}")
            print(f"Notas 50: {notas_separadas_para_saque[50]}")
            print(f"Notas 100: {notas_separadas_para_saque[100]}")
        else:
            print("\nSaque negado! Não há notas disponíveis para esta combinação de valor.")

    elif opcao == 9:
        print("Fim da operação.")
        break
    
    else:
        print("Opção Inválida! Tente novamente.")