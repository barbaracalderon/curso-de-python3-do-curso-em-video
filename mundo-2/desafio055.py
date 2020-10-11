# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

for i in range(1, 6):
    peso = float(input('Digite o peso da pessoa {}: '.format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('Maior peso: {} KG\nMenor peso: {} KG'.format(maior, menor))