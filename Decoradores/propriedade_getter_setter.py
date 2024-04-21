class Banco:
    def __init__(self, saldo):
        self._saldo = saldo
        
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, novo_saldo):
        self._saldo = novo_saldo
    
    def sacar(self):
        valor = float(input("Digite um valor de saque: "))
        if valor > self.saldo:
            print("Saldo Insuficiente")
        else:
            self.saldo -= valor
    
    def depositar(self):
        valor = float(input("Digite o valor do deposito: "))
        self.saldo += valor
            
            

p1 = Banco(400)
p1.depositar()
p1.sacar()