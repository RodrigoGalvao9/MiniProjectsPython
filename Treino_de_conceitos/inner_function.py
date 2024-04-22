#Teste 1
def funcao_externa():
    variavel = 10
    
    def funcao_interna():
        print("Este é o valor de x:", variavel)
        
    funcao_interna()
    
funcao_externa()
    
#Teste 2
class Macenaria:
    def serrar(self):
        lenha = "Serrado"
        def polindo():
            print(f"Polido e {lenha}")
        
        polindo()
        

p1 = Macenaria()
p1.serrar()

#Teste 3

def pai():
    print("Função pai")
    
    def filho1():
        print("Função filho1")
        
    def filho2():
        print("Função filho2")
        
    filho1()
    filho2()
    
pai()



#Teset 4:
def funcao_externa():
    print("Função mais externa")
    
    def funcao_interna():
        print("Função interna")
        def funcao_mais_interna():
            print("Função mais interna ainda")
        
        funcao_mais_interna()        
    funcao_interna()
    
funcao_externa()

#Teste 5

def calculo(operacao):
    def somar(a, b):
        return a + b
    
    def subtrair(a, b):
        return a - b
    
    def dividir(a, b):
        return a / b
    
    def multiplicar(a, b):
        return a * b
    
    if operacao == "+":
        return somar
    elif operacao == "-":
        return subtrair
    elif operacao == "/":
        return dividir
    elif operacao == "*":
        return multiplicar
    else:
        return exit
    
resultado = calculo("+")(4, 5)
print(resultado)    
    
    