#Teste 1
def gerar_pares(maximo):
    num = 0
    while num < maximo:
        yield num
        num += 2

# for numero in gerar_pares(10):
#     print(numero)


#Teste 2
def gerar_numeros():
    num = 1
    while True: 
        yield num
        num += 1

meu_gerador = gerar_numeros()

for _ in range(5):
    print(next(meu_gerador)) 


#Teste 3
def gerador_indices(lista):
    for i in range(len(lista)):
        yield i

nomes = ["Alice", "Bob", "Carol", "David"]

for indice in gerador_indices(nomes):
    print(nomes[indice])
