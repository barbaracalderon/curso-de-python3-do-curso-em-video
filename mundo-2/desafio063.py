# Escreva um programa que leia um número n inteiro qualquer e mostre
# na tela os n primeiros elementos de uma Sequência Fibonnaci.
# Ex.: 0, 1, 1, 2, 3, 5, 8
print('========== SEQUÊNCIA DE FIBONACCI ==========')
n = int(input('Digite quantos elementos você quer ver da Sequência de Fibonacci: '))
a = cont = 0
b = 1
while cont in range(n):
    print('{} '.format(a), end='')
    c = a + b
    a = b
    b = c
    cont +=1