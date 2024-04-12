class ReceberNumeros:
    def __init__(self):
        self.numero1 = float
        self.numero2 = float
    
    def entrada_dos_numeros_1_e_2(self):
        self.numero1 = float(input("Digite um Número:"))
        self.numero2 = float(input("Digite outro Número:"))
        

class Operacoes:
    def __init__(self):
        self.resultado = float
    
    
    def soma(self, numero1, numero2):
        self.resultado = numero1 + numero2
        

    def subtracao(self, numero1, numero2):
        self.resultado = numero1 - numero2
        
        
    def divisao(self, numero1, numero2):
        if numero1 != 0 and numero2 != 0:
            self.resultado = numero1 / numero2
        else:
            return "Erro, 0 não divisivel"
    
    def multiplicacao(self, numero1, numero2):
        self.resultado = numero1 * numero2




Usuario = ReceberNumeros()
Operador = Operacoes()

Operador.soma(Usuario.numero1, Usuario.numero2)
print(f"Resultado da Soma é: {Operador.soma}")

Operador.subtracao(Usuario.numero1, Usuario.numero2)
print(f"Resultado da Subtração é: {Operador.subtracao}")

Operador.divisao(Usuario.numero1, Usuario.numero2)
print(f"Resultado da Divisão é: {Operador.divisao}")

Operador.multiplicacao(Usuario.numero1, Usuario.numero2)
print(f"Resultado da Multiplicação é: {Operador.multiplicacao}")
