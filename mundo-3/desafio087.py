# Aprimore o desafio anterior, mostrando no final:
# a) A soma de todos os valores pares digitados;
# b) A soma dos valores da terceira coluna;
# c) O maior valor da segunda linha.
print('=============== [MATRIZ 3x3] ===============')
print('Vamos começar inserindo os dados para a sua matriz.')
linha1 = []
linha2 = []
linha3 = []
matriz = []
cont = 1
somapar = somacol = cont_linha = maior = 0
while cont < 10:
    while cont < 4:
        valor = int(input(f'Digite o {cont}ª valor: '))
        linha1.append(valor)
        if valor % 2 == 0:
            somapar += valor
        if cont == 3:
            somacol += valor
        cont += 1
    while cont < 7:
        valor = int(input(f'Digite o {cont}ª valor: '))
        linha2.append(valor)
        if valor % 2 == 0:
            somapar += valor
        if cont == 6:
            somacol += valor
        if cont_linha == 0:
            maior = valor
        elif valor > maior:
            maior = valor
        cont += 1
    while cont < 10:
        valor = int(input(f'Digite o {cont}ª valor: '))
        linha3.append(valor)
        if valor % 2 == 0:
            somapar += valor
        if cont == 9:
            somacol += valor
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
print()
print(f'A soma dos valores pares é {somapar}')
print(f'A soma dos valores da terceira coluna é {somacol}')
print(f'O maior valor da segunda linha é {maior}')