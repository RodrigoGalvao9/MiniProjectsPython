"""
Métodos de instância:

Os métodos de instância são aqueles que operam em instâncias específicas de uma classe.

Eles têm acesso aos atributos da instância através do parâmetro self, que é uma referência à própria instância.

São definidos dentro da classe e são chamados usando a notação de ponto (.) em uma instância da classe.

Os métodos de instância geralmente são usados para manipular ou interagir com os dados específicos de uma instância da classe.

"""

#Teste 1:
# class ClasseTeste:
#     def __init__(self, valor):
#         self.valor = valor
    
#     def mostrar_valor(self):
#         print("O valor é:", self.valor)

# objeto = ClasseTeste(10)

# objeto.mostrar_valor() 



#Teste 2:
PI = 3.14
class Circulo:
    def __init__(self, raio):
        self.raio = raio
        
    def area_calculo(self):
        return PI * self.raio **2
        
    def perimetro_calculo(self):
        return 2 * PI * self.raio 
        
    def raio_modificar(self, alterar):
        self.raio = alterar
        

p1 = Circulo(5)
print(f"A área do seu círculo é: {p1.area_calculo()}")
print(f"Seu perimêtro é: {p1.perimetro_calculo()}")
p1.raio_modificar(7)
print(f"Novo raio: {p1.raio}")