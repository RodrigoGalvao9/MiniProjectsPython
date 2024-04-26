nome = "João"
idade = 30
altura = 1.75
print("Olá, meu nome é {} e tenho {} anos. Minha altura é {:.2f} metros.".format(nome, idade, altura))

nome = "João"
idade = 30
print("Olá, meu nome é {} e tenho {} anos.".format(nome, idade))

numero = 3.14159
print("{:.2f}".format(numero))


print("Olá, meu nome é {nome} e tenho {idade} anos.".format(nome=nome, idade=idade))


nome = "João"
idade = 30
mensagem = "Olá, meu nome é %s e tenho %d anos." % (nome, idade)
print(mensagem)