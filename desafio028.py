# Escreva um programa que faça o computador "pensar" em um número
# inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual
# foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
num = [0, 1, 2, 3, 4, 5]
num_escolhido = random.choice(num)
num_usuario = int(input('Escolha um número entre 0 e 5: '))
if num_usuario == num_escolhido:
    print('Parabéns! Você venceu!')
else:
    print('Você perdeu.')
