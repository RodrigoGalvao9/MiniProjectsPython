class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.acelerando = False

    def buzinar(self):
        ruido = input("Você está buzinando? y/n").lower()
        while ruido == "y":
            print(f'A {self.modelo} bee-bee')
            ruido = input("Você está buzinando? y/n").lower()
        if ruido == "n":
            print(f'{self.modelo} não está buzinando')

    def parar(self):
        print(f'{self.modelo} parou')
        self.acelerando = False

    def correr(self):
        if not self.acelerando:
            print(f"{self.modelo} acelerou")
            self.acelerando = True
        else:
            print(f"{self.modelo} já está correndo")
            
            
minha_bicicleta = Bicicleta("Verde", "Caloi-900", 1999, 4000)
minha_bicicleta.buzinar()
minha_bicicleta.correr()
minha_bicicleta.parar()


            
        