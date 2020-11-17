# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
# a) quantas pessoas foram cadastradas;
# b) uma listagem com as pessoas mais pesadas;
# c) uma listagem com as pessoas mais leves.
lista = []
suporte = []
pesados = []
leves = []
cont = peso_total = 0
while True:
    nome = str(input('Nome: '))
    peso = int(input('Peso: '))
    suporte.append(nome)
    suporte.append(peso)
    lista.append(suporte[:])
    suporte.clear()
    cont += 1
    peso_total += peso
    media_peso = peso_total / cont
    continuar = str(input('Deseja continuar? [S/N]: ')).upper()[0]
    if continuar == 'N':
        break
print(f'Foram cadastradas {cont} pessoas.')
print(f'A média de pesos é {media_peso} kg')
for pessoa in lista:
    if pessoa[1] > media_peso:
        print(f'{pessoa[0]} é uma pessoa pesada.')
        pesados.append(pessoa[0])
    elif pessoa[1] < media_peso:
        print(f'{pessoa[0]} é uma pessoa leve.')
        leves.append(pessoa[0])
print(f'Pesados: {pesados}')
print(f'Leves: {leves}')