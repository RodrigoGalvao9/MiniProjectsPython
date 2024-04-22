#arg = posicional
#kwargs = (chave, valor) <- tupla

#Teste 1
def decorador(func):
    def inner_method(*args, **kwargs):
        print("Teste demais")
        func(*args, **kwargs)
        print("Oba!")
        
    return inner_method
    

@decorador
def playstation(nome):
    print(f"Olá, meu nome é: {nome}")

# playstation("Pedro")

# playstation(nome="kauê")


#Teste 2
def tecnologia(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  # Chama func e armazena o resultado
        return result  # Retorna o resultado

    return wrapper

@tecnologia
def pao(ferramenta):
    print(f"Estou usando esta ferramenta {ferramenta}")
    return ferramenta.upper()

pao("Python")
p4 = pao("python")
print(p4)
p1 = pao("pandas")
print(p1)



