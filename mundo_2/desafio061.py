# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('=========== PROGRESSÃO ARITMÉTICA ===========')
primeiro = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão dessa PA: '))
termo = 0
contador = 1
while contador <= 10:
    print('{}, '.format(termo), end='')
    termo = termo + r # Alternativa: termo += r
    contador = contador + 1
print('FIM')
