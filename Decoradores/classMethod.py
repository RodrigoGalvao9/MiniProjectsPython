class Animal:
    fazer_barulho = input("Qual o ruído que seu animal emite?")
    
    @classmethod
    def desconhecido(cls):
        anonimo = input("Digite o seu animal: ")
        print(f"{anonimo} faz {cls.fazer_barulho}")
    
    @classmethod
    def cachorro(cls):
        print(cls.fazer_barulho)
    

p1 = Animal()

p1.cachorro()
p1.desconhecido()
