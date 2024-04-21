#testando args e kwargs juntamente com o classmethod

# class Exemplo:
#     @classmethod
#     def teste_exemplo(*args, **kwargs):
#         print("Argumentos posicionais (*args)")
#         for arg in args:
#             print(arg)
            
            
#         print("\nArgumento de palavra-chave (**kwargs)")
#         for chave, valor in kwargs.items():
#             print(f"{chave}: `{valor}")
        
        

# Exemplo.teste_exemplo( 1, 2, 3, nome="Maria", idade="30")

class Exemplo:
    def teste_exemplo(*args, **kwargs):
        print("Argumentos posicionais (*args)")
        for arg in args:
            print(arg)
            
            
        print("\nArgumento de palavra-chave (**kwargs)")
        for chave, valor in kwargs.items():
            print(f"{chave}: `{valor}")
        
        

p1 = Exemplo()

p1.teste_exemplo(24, 36, 48, nome="Rodrigo", idade="18")