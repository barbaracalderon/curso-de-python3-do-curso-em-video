# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

print('========== CHECAGEM DE NÚMEROS PRIMOS ==========')
num = int(input('Digite um número inteiro: '))
if num == 1:
    print('O número {} não é primo.'.format(num))
elif num == 2 or num == 3 or num == 5 or num == 7:
    print('O número {} é primo.'.format(num))
elif num % 2 != 0: # "Crivo de Erastótenes
    if num % 3 != 0:
        if num % 5 != 0:
            if num % 7 != 0:
                print('O número {} é primo.'.format(num))
else:
    print('O numero {} não é primo.'.format(num))