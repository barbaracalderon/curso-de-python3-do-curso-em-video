# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas
# respectivas posições na lista.
lista = []
for a in range(0,5):
    lista.append(int(input(f'Digite um valor inteiro para a posição {a}: ')))
    maior = lista[0]
    menor = lista[0]
for b in lista:
    if b > maior:
        maior = b
    elif b < menor:
        menor = b
print('-'*47)
print(f'Os números digitados foram: {lista}')
print(f'O maior valor é {maior} e está na posição {lista.index(maior)}')
print(f'O menor valor é {menor} e está na posição {lista.index(menor)}')