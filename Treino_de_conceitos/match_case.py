print("""
-----------------------
   Lojinha do Rodrigo
-----------------------      

Tamanhos de roupas disponiveis:
P - Pequena
M - Média
G - Grande
      """)

tamanho = input("Qual o tamanho de roupa que procura? ").upper()

roupas = {"P":"Blusa decotada", "M": "Short Jeans-havaiana", "G":"Camisa Smash Brosh"}

match (tamanho):
    case 'P':
        print(roupas["P"])
    case 'M':
        print(roupas["M"])
    case 'G':
        print(roupas["G"])