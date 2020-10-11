# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
inicio = str(input('Vamos soltar fogos de artifício! Digite SIM para começar: ').lower())
t = 10
if inicio == 'sim':
    for i in range(0, 11):
        print(t)
        sleep(1)
        t = t - 1
    print('''              ~~~~~~~~ :::: FOGOS :::: ~~~~~~~~~
              ~~~~~~~~ ::::: DE :::::: ~~~~~~~~~
              ~~~~~~~~ :: ARTIFÍCIO :: ~~~~~~~~~''')
else:
    print('Que pena. Você não quis ver os fogos!')
        
