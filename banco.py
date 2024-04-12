# menu = """

# [d] Depositar
# [s] Sacar
# [e] Extrato
# [q] Sair

# => """

# saldo = 0
# limite = 500
# extrato = ""
# numero_saques = 0
# LIMITE_SAQUES = 3

# while True:

#     opcao = input(menu)

#     if opcao == "d":
#         valor = float(input("Informe o valor do depósito: "))

#         if valor > 0:
#             saldo += valor
#             extrato += f"Depósito: R$ {valor:.2f}\n"

#         else:
#             print("Operação falhou! O valor informado é inválido.")

#     elif opcao == "s":
#         valor = float(input("Informe o valor do saque: "))

#         excedeu_saldo = valor > saldo

#         excedeu_limite = valor > limite

#         excedeu_saques = numero_saques >= LIMITE_SAQUES

#         if excedeu_saldo:
#             print("Operação falhou! Você não tem saldo suficiente.")

#         elif excedeu_limite:
#             print("Operação falhou! O valor do saque excede o limite.")

#         elif excedeu_saques:
#             print("Operação falhou! Número máximo de saques excedido.")

#         elif valor > 0:
#             saldo -= valor
#             extrato += f"Saque: R$ {valor:.2f}\n"
#             numero_saques += 1

#         else:
#             print("Operação falhou! O valor informado é inválido.")

#     elif opcao == "e":
#         print("\n================ EXTRATO ================")
#         print("Não foram realizadas movimentações." if not extrato else extrato)
#         print(f"\nSaldo: R$ {saldo:.2f}")
#         print("==========================================")

#     elif opcao == "q":
#         break

#     else:
#         print("Operação inválida, por favor selecione novamente a operação desejada.")



class Menu:
    
    @staticmethod
    def menu_inicial():
            while True:
                print("----- Menu Principal -----")
                print("""[d] Depositar
                        [s] Sacar
                        [e] Extrato
                        [q] Sair
                      """)
                
                opcao = input("Escolha uma opção: ").lower()
                
                if opcao == 'd':
                    #chamar método da classe deposito
                elif opcao == 's':
                    #chamar método da classe saque
                elif opcao == 'e':
                    #chamar método da classe extrato
                elif opcao == 'q':
                    print("Encerrando sistema...")
                    break
                else:
                    print("Opção inválida. Por favor escolha uma opção válida!")
                

class Banco:
    
    @staticmethod
    def depositar(saldo,valor, extrato):
        saldo += valor
        extrato.append(f"Déposito de `{valor}")
        print(f"Depósito de {valor}, realizado com sucesso!")
        print(f"Seu saldo atual é: {saldo}")   
        
    @staticmethod
    def sacar(saldo, valor, extrato, numero_saques, limite_saques):
        
        limite_saques = 3
        print("Só pode ser realizado 3 saques por vez!!")
        try:
            numero_saques = int(input("Quantos saques você vai realizar? "))
        except ValueError:
            print("Por favor, insira um número inteiro válido.")
        
        
        if numero_saques <= limite_saques:
            for i in range(numero_saques):
                valor = float(input("Digite o valor do seu saque:"))
                if valor <= saldo:
                    saldo -= valor
                    extrato.append(f"Saque de {valor}")
                    print("Realizado com sucesso!!")
                else:
                    print("Seu saldo é menor que o valor do saque!")
                    return (f"Seu saldo atual é: {saldo}")
        else:
            print("Você excedeu o numeros limite de saques!")
        

    @staticmethod
    def exibir_extrato(saldo, extrato):
        print("----- Extrato -----")
        print(f"Saldo atual: {saldo}")
        print("Transações:")
        for transacao in extrato:
            print(transacao)
        
    


class Usuario:
    
    def criar_usuario(usuarios):
        try:
            novo_usuario = input("Digite o nome do seu usuário").lower()
            cpf = input("Digite seu cpf:")
            if novo_usuario in usuarios:
                print("Esse usuário já existe!!")
            elif len(cpf) != 9 or not cpf.isnumeric():
                print("O cpf deve conter 9 números")
            else:
                usuarios[novo_usuario] = cpf
        except Exception as e:
            print(f"Ocorreu um erro {e}")
        
    def filtrar_usuario(cpf, usuarios):
        try:
            
        
        
    def criar_contas(agencia, numero_conta, usuarios):
        
        
        
    def listar_contas(contas):
        
        
        
        
        
        
        
        