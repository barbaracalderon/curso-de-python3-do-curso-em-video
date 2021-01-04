# Faça um programa que calcule a soma entre todos os números ímpares que
# são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0
for i in range(1, 500, 2):
    if i % 3 == 0:
        soma = soma + i
print('Soma de todos os números ímpares, e múltiplos de 3, do intervalo de 1 a 500: {}.'.format(soma))