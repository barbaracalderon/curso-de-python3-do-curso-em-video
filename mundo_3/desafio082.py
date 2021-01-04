# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas
# listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.
lista = []
pares = []
impares = []
while True:
    num = int(input('Digite um valor: '))
    continuar = str(input('Deseja continuar? [S/N]: ')).upper()[0]
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    if continuar == 'N':
        break
print('=============== [RELATÓRIO] ==================')
print(f'A lista comple é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')