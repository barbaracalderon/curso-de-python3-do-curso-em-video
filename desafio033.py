# Faça um programa que leia três números e mostre
# qual é o maior e qual é o menor.

num_1 = int(input('Digite um número: '))
num_2 = int(input('Digite um segundo número: '))
num_3 = int(input('Digite um terceiro número: '))

if num_1 > num_2 and num_1 > num_3:
    print('Esse é o maior número: {}'.format(num_1))
elif num_2 > num_1 and num_2 > num_3:
    print('Esse é o maior número: {}'.format(num_2))
else:
    print('Esse é o maior número: {}'.format(num_3))

if num_1 < num_2 and num_1 < num_3:
    print('Esse é o menor número: {}'.format(num_1))
elif num_2 < num_1 and num_2 < num_3:
    print('Esse é o menor número: {}'.format(num_2))
else:
    print('Esse é o menor número: {}'.format(num_3))