# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro de uma lista e a segunda função
# vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
num = 0
numeros = []
def sorteia(num):
    for d in range(0, 5):
        valor = randint(0, 100)
        numeros.append(valor)
    print('=========== [SORTEIO DE NÚMEROS] ===========')
    print('Os números sorteados foram: ')
    for n in numeros:
        print(f'{n} -> ', end="")
    print('FIM')

def somaPar(numero):
    soma = 0
    copia = numeros[:]
    pares = []
    print('============= [SOMA DOS PARES] =============')
    for p in copia:
        if p % 2 == 0:
            pares.append(p)
            soma += p
    print(f'Valores pares: {pares}', end="")
    print(f'\nA soma dos valores pares é {soma}')


# Programa Principal
sorteia(num)
somaPar(num)
print('--------------------------------------------')
print('<< ENCERRADO >>')
