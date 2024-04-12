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



import re

class Menu:
    
    @staticmethod
    def menu_inicial():
        while True:
            print("----- Menu Principal -----")
            print("""
                    [d] Depositar
                    [s] Sacar
                    [e] Extrato
                    [q] Sair
                  """)
            
            opcao = input("Escolha uma opção: ").lower()
            
            if opcao == 'd':
                Banco.depositar()
            elif opcao == 's':
                Banco.sacar()
            elif opcao == 'e':
                Banco.exibir_extrato()
            elif opcao == 'q':
                print("Encerrando sistema...")
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida!")


class Banco:
    
    saldo = 0
    extrato = []
    limite_saques = 3
    
    @staticmethod
    def depositar():
        try:
            valor = float(input("Digite o valor a depositar: "))
            Banco.saldo += valor
            Banco.extrato.append(f"Déposito de {valor}")
            print(f"Depósito de {valor}, realizado com sucesso!")
            print(f"Seu saldo atual é: {Banco.saldo}")
        except ValueError:
            print("Por favor, insira um valor numérico válido.")

    @staticmethod
    def sacar():
        try:
            print("Só podem ser realizados 3 saques por vez!")
            numero_saques = int(input("Quantos saques você vai realizar? "))
            if numero_saques <= Banco.limite_saques:
                for _ in range(numero_saques):
                    valor = float(input("Digite o valor do seu saque: "))
                    if valor <= Banco.saldo:
                        Banco.saldo -= valor
                        Banco.extrato.append(f"Saque de {valor}")
                        print("Saque realizado com sucesso!")
                    else:
                        print("Seu saldo é menor que o valor do saque!")
            else:
                print("Você excedeu o número limite de saques!")
        except ValueError:
            print("Por favor, insira um valor numérico válido para o número de saques.")

    @staticmethod
    def exibir_extrato():
        print("----- Extrato -----")
        print(f"Saldo atual: {Banco.saldo}")
        print("Transações:")
        for transacao in Banco.extrato:
            print(transacao)


class Usuario:
    
    @staticmethod
    def criar_usuario(usuarios):
        try:
            novo_usuario = input("Digite o nome do seu usuário: ").lower()
            cpf = input("Digite seu CPF: ")
            if novo_usuario in usuarios:
                print("Esse usuário já existe!!")
            elif not re.match(r'^\d{9}$', cpf):
                print("O CPF deve conter exatamente 9 números.")
            else:
                usuarios[novo_usuario] = cpf
        except Exception as e:
            print(f"Ocorreu um erro {e}")

    @staticmethod
    def filtrar_usuario(usuarios):
        try:
            cpf = input("Digite o CPF do usuário que você quer filtrar: ")
            for nome, cpf_usuario in usuarios.items():
                if cpf_usuario == cpf:
                    return f"Este é o usuário que você procurou: {nome}"
            print("Usuário não encontrado.")
        except Exception as e:
            print(f"Algum erro ocorreu! {e}")

    @staticmethod
    def criar_contas(contas_existentes, usuarios):
        try:
            criar_contas = input("Você deseja criar uma conta? (y/n)").lower()
            if criar_contas == "y":
                nome_usuario = input("Digite o nome do usuário para criar a conta: ").lower()
                if nome_usuario in contas_existentes:
                    print("Esse usuário já possui uma conta!")
                    return
                agencia = input("Digite o número da agência: ")
                numero_conta = input("Digite o número da conta: ")
                contas_existentes[nome_usuario] = {"agencia": agencia, "numero_conta": numero_conta}
                print("Conta criada com sucesso!")
            else:
                print("Criação de conta cancelada.")
        except Exception as e:
            print(f"Ocorreu um erro ao criar a conta: {e}")

    @staticmethod
    def listar_contas(contas_existentes):
        try:
            nome_conta = input("Digite o nome da conta que você quer procurar: ").lower()
            informacoes_conta = contas_existentes.get(nome_conta)
            if informacoes_conta:
                print(f"Informações da conta para {nome_conta}: {informacoes_conta}")
            else:
                print("Conta não encontrada.")
        except Exception as e:
            print(f"Ocorreu um erro ao listar a conta: {e}")


# Exemplo de uso:
usuarios = {}
contas_existentes = {}

Menu.menu_inicial()
