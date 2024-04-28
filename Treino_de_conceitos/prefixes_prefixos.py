#Prefiro r = Raw
#Ex:
variavel = r'C:\Users\Username\Documents'
#os escapes de caractere não são interpretados



#Prefixo b = Bytes literais
#Ex:
data = b'Hello World'
#indica que o "Literal" é uma sequencia de bytes invés de uma string unicode

#Prefixo u = Strings unicodes(foi descontinuado, versão 2 do python)
#Ex:
text = u'Olá Mundo'
#Indicava que era uma string unicode, como se sabe toda string no python versão 3 já interpretada padrão como unicode

#Prefixo f = formatação
#Ex:
name = 'Alice'
age = 30
message = f'Meu nome é {name} e tenho {age} anos.'
#Basicamente é parte do conceito de interpolação

#Prefixo 'Ob, 'Oo', 'Ox' = Binarios, octanais e hexadecimais
#Ex:
binary = 0b1010  # Representa o número binário 1010
octal = 0o12     # Representa o número octal 12 (equivalente a 10 em decimal)
hexa = 0x1F      # Representa o número hexadecimal 1F (equivalente a 31 em decimal)
#Usado para representas números em diferentes bases númericas

#artigo do stackoverflow usado como base:
#https://pt.stackoverflow.com/questions/255271/quais-s%C3%A3o-e-qual-a-fun%C3%A7%C3%A3o-de-cada-prefixo-de-string-no-python