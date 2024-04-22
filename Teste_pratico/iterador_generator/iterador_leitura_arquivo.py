class IteradorArquivo:
    def __init__(self, nome_arquivo):
        self.file = open(nome_arquivo)
        
    def __iter__(self):
        return self
    
    def __next__(self):
        linha = self.file.readline()
        if linha != '':
            return linha
        else:
            self.file.close()
            raise StopIteration
            
 
for linha in IteradorArquivo(r'C:\Users\rodri\Área de Trabalho\codigo\MiniProjectsPython\Teste_pratico\iterador_generator\testeIterador.txt'):
    print(linha)