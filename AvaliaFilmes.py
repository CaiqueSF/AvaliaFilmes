# Avaliação Filmes**************************************************************************************
'''
Desenvolva novas funcionalidades para complementar o gerenciamento da classe Filmes. 
Segue o escopo das funcionalidades:

    1. Uma das funcionalidades requeridas é que o usuário possa realizar a avaliação de um filme 
    passando uma nota com parâmetro e que essa nota seja salva no atributo específico da classe.

    2. Assim que uma avaliação for realizada, deve ser incrementado o total de avaliadores daquele filme. 
    Obs: Considere criar um atributo específico para esse fim.
    
    3. Para cada filme ter uma nota de avaliação média que consiste na divisão do total de avaliação 
    pelo total de avaliadores.
'''
import statistics as sta

# CLASSE
class Filme:
    # Método Cosntrutor
    def __init__(self, nome, lancamento, inclusoPlano, nota, avaliadores, avaliaMedia, duracaoMin):
        self.nome = nome
        self.lancamento = lancamento
        self.inclusoPlano = inclusoPlano
        self.nota = nota 
        self.avaliadores = avaliadores
        self.avaliaMedia = avaliaMedia
        self.duracaoMin = duracaoMin
        
    def  fichaTecnica(self):
        print('==========DADOS DO FILME==========')
        print(f'• Nome do filme: {self.nome}')
        print(f'• Ano de lançamento: {self.lancamento}')
        print(f'• Filme está no plano? {self.inclusoPlano}')
        print(f'• Avaliação do filme: {self.nota}')
        print(f'• Total de avaliadores: {self.avaliadores}')
        print(f'• Média das avaliações: {self.avaliaMedia}')
        print(f'• Duração do filme: {self.duracaoMin}\n')

# VARIÁVEIS
continua = 's'
notaMario = []
notaAvatar = []
avaliadores = 0

# LAÇO DE REPETIÇÃO
while continua.lower() != 'n':
    avaliaMario = float(input('\nNota para o filme Mário Bros: '))
    notaMario.append(avaliaMario)
    avaliaAvatar = float(input('Nota para o filme Avatar 2: '))
    notaAvatar.append(avaliaAvatar)
    
    avaliadores+=1
    
    mario = Filme('Super Mário Bros', 2023, False, sum(notaMario), avaliadores, sta.mean(notaMario), 125)
    avatar = Filme('Avatar 2', 2023, False, sum(notaAvatar), avaliadores, sta.mean(notaAvatar), 175)
    mario.fichaTecnica()
    avatar.fichaTecnica()
    
    continua = input('DESEJA AVALIAR NOVAMENTE? (s: sim | n: não): ')
