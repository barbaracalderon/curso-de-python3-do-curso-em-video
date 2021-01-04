# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
# a) quantas pessoas foram cadastradas;
# b) uma listagem com as pessoas mais pesadas;
# c) uma listagem com as pessoas mais leves.
lista = []
suporte = []
maior = menor = 0
while True:
    suporte.append(str(input('Nome: ')))
    suporte.append(float(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = suporte[1]
    else:
        if suporte[1] > maior:
            maior = suporte[1]
        elif suporte[1] < menor:
            menor = suporte[1]
    lista.append(suporte[:])
    suporte.clear()
    continuar = str(input('Deseja continuar? [S/N]: ')).upper()[0]
    if continuar == 'N':
        break
print('====================== [RELATÓRIO] =========================')
print(f'Foram cadastradas {len(lista)} pessoas.')
for pessoa in lista:
    if pessoa[1] == maior:
        print(f'Mais pesado: {pessoa[0]}')
    if pessoa[1] == menor:
        print(f'Mais leve: {pessoa[0]}')