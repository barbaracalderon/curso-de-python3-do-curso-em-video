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
        valor = str(input(f'Digite o {cont}ª valor: '))
        linha1.append(valor)
        cont += 1
    while cont < 7:
        valor = str(input(f'Digite o {cont}ª valor: '))
        linha2.append(valor)
        cont += 1
    while cont < 10:
        valor = str(input(f'Digite o {cont}ª valor: '))
        linha3.append(valor)
        cont += 1
    matriz.append(linha1)
    matriz.append(linha2)
    matriz.append(linha3)
print(matriz)