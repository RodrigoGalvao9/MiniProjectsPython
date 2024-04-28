class MeuIterador:
    def __init__(self):
        self.num = 10

    def __iter__(self):
        return self

    def __next__(self):
        if 11> self.num >0:
            resultado = self.num
            self.num -= 1
            return resultado
        else:
            raise StopIteration

iterador = MeuIterador()

for elemento in iterador:
    print(elemento)
    
