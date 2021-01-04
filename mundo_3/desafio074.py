# Crie um programa que vai gerar cinco números aleatórios e colocar
# em uma tupla. Depois disso, mostre a listagem de números gerados e
# também indique o menor e o maior valor que estão na tupla.
from random import randint
print('================== [NÚMEROS ALEATÓRIOS] ===================')
tupla = (randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100))
print(f'Números gerados aleatoriamente: {tupla}')
print(f'Maior valor: {sorted(tupla)[-1]}')
print(f'Menor valor: {sorted(tupla)[0]}')