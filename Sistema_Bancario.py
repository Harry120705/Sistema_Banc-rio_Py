menu = '''    ========================
            Menu
        [d] Deposito
        [s] Saque
        [e] Extrato
        [q] Sair
    ========================
Operação desejada:'''
msg_boas_vindas = '''Seja bem Vindo ao nosso Sistema!'''

saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_DE_SAQUES = 3


print(msg_boas_vindas)
while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Digite o valor desejado para o deposito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            
        else:
            print("Deposito falhou!, o valor informado é inválido!")


    elif opcao == "s":
        valor_saque = float(input("Digite o valor do saque: "))
        
        excedeu_saldo = valor_saque > saldo
        
        excedeu_limite = valor_saque > limite
        
        excedeu_saques = numero_de_saques >= LIMITE_DE_SAQUES
                
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente")
            
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excedeu o limite")
            
        elif excedeu_saques:
            print("Operação falhou! Excedeu o limite de saques")
        
        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            numero_de_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido")
    
    elif opcao == "e":
        print("\n =============EXTRATO==========")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("=====================================================")
        
    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        
print("Obrigado por utilizar nosso sistema, até uma próxima vez!")