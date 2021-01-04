# Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores
# lidos pelo teclado. No final, mostre a matriz na tela com a formatação correta.
print('=============== [MATRIZ 3x3] ===============')
print('Vamos começar inserindo os dados para a sua matriz.')
linha1 = []
linha2 = []
linha3 = []
matriz = []
cont = 1
while cont < 10:
    while cont < 4:
        valor = int(input(f'Digite o {cont}ª valor: '))
        linha1.append(valor)
        cont += 1
    while cont < 7:
        valor = int(input(f'Digite o {cont}ª valor: '))
        linha2.append(valor)
        cont += 1
    while cont < 10:
        valor = int(input(f'Digite o {cont}ª valor: '))
        linha3.append(valor)
        cont += 1
    matriz.append(linha1)
    matriz.append(linha2)
    matriz.append(linha3)
print('===========================================')
for e in matriz[0]:
    print(f'[{e:^5}]', end=' ')
print()
for f in matriz[1]:
    print(f'[{f:^5}]', end=' ')
print()
for g in matriz[2]:
    print(f'[{g:^5}]', end=' ')

'''
Uma outra forma de realizar esse exercício, mostrada pelo prof. Guanabara, é a seguinte:
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
    matriz[l][c] = int(input(f'Digite um valor para [{l}], [{c}]: '))
print('=-' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5]', end='')
    print()
'''