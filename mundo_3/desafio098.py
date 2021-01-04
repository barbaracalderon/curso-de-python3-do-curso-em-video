# Faça um programa que tenha a função chamada contador(), que receba três parâmetros:
# início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1;
# b) de 10 até 0, de 2 em 2;
# c) uma contagem personalizada.
from time import sleep
def contador(i, f, p):
    print(f'<< CONTAGEM DE {i} ATÉ {f}, DE {p} EM {p} >>')
    if i > f:
        p = -p
        for c in range(i, f + p, p):
            print(f'{c} -> ', end='')
        print('FIM')
        print('--------------------------------------------')
    else:
        for c in range(i, f + p, p):
            print(f'{c} -> ', end='')
        print('FIM')
        print('--------------------------------------------')

# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
inicio = int(input('Início da contagem: '))
fim = int(input('Fim da contagem: '))
passo = int(input('Passo: '))
if passo < 0:
    passo *= -1
if passo == 0:
    passo = 1
contador(inicio, fim, passo)
