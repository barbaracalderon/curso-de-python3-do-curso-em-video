# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em
# uma lista única que mantenha separado os valores pares e ímpares. No final, mostre os
# valores pares e ímpares em ordem crescente.
lista = []
pares = []
impares = []
for v in range(0, 7):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
pares.sort()
impares.sort()
lista.append(pares)
lista.append(impares)
print(f'Em ordem crescente:')
print(f'Lista de valores pares é {lista[0]}')
print(f'Lista de valores ímpares é {lista[1]}')