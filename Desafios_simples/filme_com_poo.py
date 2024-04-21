class Filme:
    def __init__(self, titulo, genero, ano, indicacao_crianca):
        self.titulo = titulo
        self.genero = genero
        self.ano = ano
        self.indicacao_crianca = indicacao_crianca

class SistemaAvaliacaoFilmes:
    def __init__(self):
        self.filmes = []

    def adicionar_filme(self, filme):
        self.filmes.append(filme)

    def listar_filmes(self):
        for filme in self.filmes:
            print("Título:", filme.titulo)
            print("Gênero:", filme.genero)
            print("Ano:", filme.ano)
            print("Indicação para crianças:", "Sim" if filme.indicacao_crianca else "Não")
            print()

    def verificar_indicacao_crianca(self, genero):
        generos_indicativos_crianca = ['animação', 'infantil', 'família']
        for genero_indicativo in generos_indicativos_crianca:
            if genero_indicativo.lower() in genero.lower():
                return True
        return False

if __name__ == "__main__":
    sistema = SistemaAvaliacaoFilmes()
    
    while True:
        titulo = input("Digite o título do filme (ou deixe em branco para encerrar): ")
        if not titulo:
            break
        genero = input("Digite o gênero do filme: ")
        ano = int(input("Digite o ano de lançamento do filme: "))
        
        indicacao_crianca = sistema.verificar_indicacao_crianca(genero)
        
        filme = Filme(titulo, genero, ano, indicacao_crianca)
        sistema.adicionar_filme(filme)
    
    print("Filmes cadastrados:")
    sistema.listar_filmes()



# Crie uma classe(objeto) chamada "Filme" que tenha:
#     - Um título
#     - Um gênero
#     - Um ano de lançamento
#     - Uma indicação de ser para crianças ou não

# Crie uma classe chamada "Sistema de Avaliação de Filmes" que tenha:
#     - Uma lista de filmes

#     Um método Para adicionar um filme à lista de filmes:
#         Adicione o filme à lista

#     Um método Para listar todos os filmes na lista:
#         Para cada filme na lista:
#             Mostre o título do filme
#             Mostre o gênero do filme
#             Mostre o ano de lançamento do filme
#             Mostre se é indicado para crianças ou não

#     Um método Para verificar se um gênero é para crianças:
#         Se o gênero incluir palavras como "animação", "infantil" ou "família":
#             Retorne verdadeiro
#         Senão:
#             Retorne falso

# Crie um "Sistema de Avaliação de Filmes"

# Enquanto Verdadeiro:
#     Pergunte pelo título do filme (ou deixe em branco para terminar)
#     Se o título estiver em branco:
#         Encerre o "programa, sejá como você queira chamar né kkkkk"
#     Pergunte pelo gênero do filme
#     Pergunte pelo ano de lançamento do filme
#     Verifique se o gênero é para crianças ou não
#     Adicione o filme ao "Sistema de Avaliação de Filmes"

# Mostre todos os filmes do "Sistema de Avaliação de Filmes"
