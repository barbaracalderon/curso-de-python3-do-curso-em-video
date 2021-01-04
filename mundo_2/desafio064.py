# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre
# eles (desconsiderando a flag).
contador = num = soma = 0
print('============ CONTADOR DE NÚMEROS =============')
print('Vamos somar os números! Para parar de inserir números ("flag"), digite "999".')
while num != 999:
    num = int(input('Digite um número: '))
    contador += 1
    soma += num
if num == 999:
    soma -= 999
    contador -= 1
print('Você digitou {} números e a soma entre eles foi {}.'.format(contador, soma))