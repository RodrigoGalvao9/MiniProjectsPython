#teste de herança multipla e abreviaçao de argumento chave: kwargs assim como a função stattr

class Animal:
    def __init__(self, numero_patas, **kwargs):
        self.numero_patas = numero_patas
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, cor_pelo, viviparo, **kwargs):
        super().__init__(**kwargs)
        self.cor_pelo = cor_pelo
        self.viviparo = viviparo

class Ave(Animal):
    def __init__(self, cor_das_penas, oviparo, **kwargs):
        super().__init__(**kwargs)
        self.cor_das_penas = cor_das_penas
        self.oviparo = oviparo
    
class Gato(Mamifero):
    def __init__(self, raca, **kwargs):
        super().__init__(**kwargs)
        self.raca = raca

class Tucano(Ave):
    def __init__(self, raca, **kwargs):
        super().__init__(**kwargs)
        self.raca = raca
        
class Onitorrinco(Mamifero, Ave):
    def __init__(self, veneno, cauda, **kwargs):
        super().__init__(**kwargs)
        self.veneno = veneno
        self.cauda = cauda

# Exemplo de uso
jerry = Onitorrinco(veneno=True, cauda='longa', cor_pelo='marrom', viviparo=True, cor_das_penas='colorido', oviparo=False, numero_patas=4)
zulu = Tucano(cor_das_penas='colorido', oviparo=True, numero_patas=2, raca="Pedreiro")
cleiton = Gato(raca='Siamês', cor_pelo='branco', viviparo=True, numero_patas=4)

print(jerry)
print(zulu)
print(cleiton)

