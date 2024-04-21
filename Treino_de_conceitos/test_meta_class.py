#Treino da função super

# class Pai:
#     def saudacao(self):
#         return 'Olá do pai'
    
# class Filho(Pai):
#     def saudacao(self):
#         return super().saudacao() + " - Olá do filho"
    
# f = Filho()
# print(f.saudacao())



# Treino de Metaclass

# class TesteMetaClass(type):
#     def __new__(cls, nome, bases, dct):
#         dct['novo_atributo'] = 100
#         return super().__new__(cls, nome, bases, dct)
    
    
# class MinhaClasse(metaclass=TesteMetaClass):
#     pass    

# print(MinhaClasse.novo_atributo)



