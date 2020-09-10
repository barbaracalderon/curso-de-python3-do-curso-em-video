# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

ano = float(input('Digite um ano: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Esse ano é BISSEXTO!')
else:
    print('Esse ano não é bissexto.')