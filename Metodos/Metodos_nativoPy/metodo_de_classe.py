"""


"""


#teste 1
class MinhaClasse:
    contador = 0
    
    def __init__(self):
        MinhaClasse.contador += 1

    @classmethod
    def obter_contador(cls):
        return cls.contador

print(MinhaClasse.obter_contador())