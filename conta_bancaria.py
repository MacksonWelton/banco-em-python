menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] sair
=> """

saldo = 0
limite = 500.00
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def deposito(saldo, valor):    
    global extrato

    if valor > 0:
        saldo += valor
        converted_valor = float(valor)
        extrato += f"Depósito: R$ {converted_valor:.2f}\n"
    else:
        print("Operação Inválida! Valor deve ser maior que zero")

def saque(saldo, valor, limite, numero_saques, LIMITE_SAQUES):
    global extrato
    
    if valor > saldo:
        print(f"Operação Inválida! O valor não pode ser maior que o saldo. Saldo: R$ {saldo:.2f}")
    elif numero_saques >= LIMITE_SAQUES:
        print(f"Operação Inválida! Você excedeu o limite de saques. Limite de Saques: {LIMITE_SAQUES}")
    elif valor > limite:
        print(f"Operação Inválida! Valor não pode ser maior que R$ {limite:.2f}")
    else:
        saldo -= valor
        numero_saques += 1
        extrato += f"Saque: R$ {valor:.2f}\n"

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        valor = float(input("Digite o valor de depósito: "))
        deposito(saldo, valor)

    elif opcao == "s":
        print("Saque")
        valor = float(input("Digite o valor de saque: "))
        saque(saldo, valor, limite, numero_saques, LIMITE_SAQUES)

    elif opcao == "e":
        print("========================== Extrato ==========================")
        print("Sem movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=============================================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")