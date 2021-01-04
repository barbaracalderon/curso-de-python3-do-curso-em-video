# Faça um programa que ajude um jogador da MEGASENA a criar palpites. O programa vai perguntar quantos jogos
# serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
lista = []
palpite = []
valor = 0
cont = 1
quantidade = int(input('Digite quantos jogos deseja: '))
print('================ JOGOS MEGASENA ================')
for p in range(0, quantidade):
    while cont < 7:
        valor = randint(1, 60)
        if valor not in palpite:
            palpite.append(valor)
            cont += 1
    palpite.sort()
    lista.append(palpite[:])
    palpite.clear()
    cont = 1
    print(f'Jogo {p+1}: {lista[p]}')
    sleep(0.5)