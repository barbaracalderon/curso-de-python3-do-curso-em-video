# Escreva um programa que leia dois números inteiros e compare-os,
# mostrando na tela a mensagem:
# a) O primeiro valor é maior;
# b) O segundo valor é maior;
# c) Não existe valor maior, os dois são iguais.

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
if a > b:
    print('O primeiro valor ({}) é o maior.'.format(a))
elif b > a:
    print('O segundo valor ({}) é o maior.'.format(b))
else:
    print('Não existe valor maior, os dois são iguais.')