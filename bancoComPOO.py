import re
DIGITE_NOME_CONTA = "Digite o nome da conta:"
CONTA_NAO_ENCONTRADA = "Conta não encontrada"

class Menu:
    
    @staticmethod
    def menu_inicial():
        while True:
            print("----- Menu Principal -----")
            print("""
                    [d] Depositar
                    [s] Sacar
                    [e] Extrato
                    [c] Criar Conta
                    [q] Sair
                  """)
            
            opcao = input("Escolha uma opção: ").lower()
            
            if opcao == 'd':
                nome_conta = input(DIGITE_NOME_CONTA)
                Banco.depositar(nome_conta)
            elif opcao == 's':
                nome_conta = input(DIGITE_NOME_CONTA)
                Banco.sacar(nome_conta)
            elif opcao == 'e':
                nome_conta = input(DIGITE_NOME_CONTA)
                Banco.exibir_extrato(nome_conta)
            elif opcao == 'c':
                Usuario.criar_conta()
            elif opcao == 'q':
                print("Encerrando sistema...")
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida!")


class Banco:
    
    @staticmethod
    def depositar(nome_conta):
        try:
            valor = float(input("Digite o valor a depositar: "))
            usuario = Usuario()
            if usuario.conta_existe(nome_conta):
                usuario.depositar_conta(nome_conta, valor)
            else:
                print(CONTA_NAO_ENCONTRADA)
        except ValueError:
            print("Por favor, insira um valor numérico válido.")

    @staticmethod
    def sacar(nome_conta):
        try:
            usuario = Usuario()
            if usuario.conta_existe(nome_conta):
                valor = float(input("Digite o valor a ser sacado: "))
                usuario.sacar_conta(nome_conta, valor)
            else:
                print(CONTA_NAO_ENCONTRADA)
        except ValueError:
            print("Por favor, insira um valor numérico válido.")

    @staticmethod
    def exibir_extrato(nome_conta):
        usuario = Usuario()
        if usuario.conta_existe(nome_conta):
            usuario.exibir_extrato_conta(nome_conta)
        else:
            print(CONTA_NAO_ENCONTRADA)


class Usuario:
    
    def __init__(self):
        self.usuarios = {}
        self.contas_existentes = {}

    def criar_usuario(self):
        try:
            novo_usuario = input("Digite o nome do seu usuário: ").lower()
            cpf = input("Digite seu CPF: ")
            if novo_usuario in self.usuarios:
                print("Esse usuário já existe!!")
            elif not re.match(r'^\d{9}$', cpf):
                print("O CPF deve conter exatamente 9 números.")
            else:
                self.usuarios[novo_usuario] = cpf
        except Exception as e:
            print(f"Ocorreu um erro {e}")

    def criar_conta(self):
        try:
            nome_usuario = input("Digite o nome do usuário para associar a conta: ").lower()
            if nome_usuario in self.usuarios:
                nome_conta = input(DIGITE_NOME_CONTA)
                if nome_conta not in self.contas_existentes:
                    agencia = input("Digite o número da agência: ")
                    numero_conta = input("Digite o número da conta: ")
                    self.contas_existentes[nome_conta] = {"usuario": nome_usuario, "agencia": agencia, "numero_conta": numero_conta, "saldo": 0, "extrato": []}
                    print("Conta criada com sucesso!")
                else:
                    print("Essa conta já existe!")
            else:
                print("Usuário não encontrado.")
        except Exception as e:
            print(f"Ocorreu um erro ao criar a conta: {e}")

    def listar_contas(self):
        nome_usuario = input("Digite o nome do usuário para listar suas contas: ").lower()
        contas_usuario = [conta for conta, dados in self.contas_existentes.items() if dados["usuario"] == nome_usuario]
        if contas_usuario:
            print(f"Contas de {nome_usuario}:")
            for conta in contas_usuario:
                print(conta)
        else:
            print("Usuário não possui contas.")
    
    def conta_existe(self, nome_conta):
        return nome_conta in self.contas_existentes
    
    def depositar_conta(self, nome_conta, valor):
        self.contas_existentes[nome_conta]["saldo"] += valor
        self.contas_existentes[nome_conta]["extrato"].append(f"Depósito de {valor}")
        print("Depósito realizado com sucesso!")
        
    def sacar_conta(self, nome_conta, valor):
        if valor <= self.contas_existentes[nome_conta]["saldo"]:
            self.contas_existentes[nome_conta]["saldo"] -= valor
            self.contas_existentes[nome_conta]["extrato"].append(f"Saque de {valor}")
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente.")
            
    def exibir_extrato_conta(self, nome_conta):
        print("----- Extrato -----")
        print(f"Saldo atual: {self.contas_existentes[nome_conta]['saldo']}")
        print("Transações:")
        for transacao in self.contas_existentes[nome_conta]["extrato"]:
            print(transacao)


# Exemplo de uso:
usuarios = {}
contas_existentes = {}

Menu.menu_inicial()

