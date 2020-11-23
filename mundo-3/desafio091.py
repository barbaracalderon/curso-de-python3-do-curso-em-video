# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses
# resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que
# o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter
dado = {}
maior = 0
dado["Jogador_1"] = randint(1, 6)
dado["Jogador_2"] = randint(1, 6)
dado["Jogador_3"] = randint(1, 6)
dado["Jogador_4"] = randint(1, 6)
print('========= [CAMPEONATO - JOGO DE DADOS] ==========')
for k, v in dado.items():
    print(f'O {k} fez {v} pontos no dado.')
print('================== RANKING ======================')
ranking = []
ranking = sorted(dado.items(), key=itemgetter(1), reverse=True) # Valor 1 no "itemgetter" significa que vai pegar pelo valor. Para pegar pela chave seria 0
for i, v in enumerate(ranking):
    print(f'{i+1}º LUGAR: {v[0]} = {v[1]} pontos!')
    sleep(0.5)
print('<< PARABÉNS! >>')
