# Faça um programa que leia algo pelo teclado e mostre na tela
# o seu tipo primitivo e todas as informações possíveis sobre ele.

algo = input('Digite algo: ')
print('O tipo primitivo de "algo" é: ', type(algo))
print('Só tem espaços? ', algo.isspace())
print('É um número? ', algo.isnumeric())
print('É um alfabético? ', algo.isalpha())
print('É alfanumérico? ', algo.isalnum())
print('Está em maiúsculas?', algo.isupper())
print('Está em minúsculas?', algo.islower())
print('Está capitalizada?', algo.istitle())
