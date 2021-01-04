# Escreva um programa que leia um número inteiro qualquer e peça para
# o usuário escolher qual será a base de conversão:
# 1 - para binário;
# 2 - para octal;
# 3 - para hexadecimal.

decimal = int(input('Digite um número inteiro qualquer: '))
escolha = int(input('Para fazer as conversões, digite \n1 para BINÁRIO, \n2 para OCTAL ou \n3 para HEXADECIMAL: '))
if escolha == 1:
    print('O número {} convertido em binário: {}'.format(decimal, bin(decimal)[2:]))
elif escolha == 2:
    print('O número {} convertido em octal: {}'.format(decimal, oct(decimal)[2:]))
elif escolha == 3:
    print('O número {} convertido em hexadecimal: {}'.format(decimal, hex(decimal)[2:]))
else:
    print('Valor inválido.')

# Em Python, para valores binários, octais e hexadecimais aparece
# dois dígitos na frente do valor: 0b, 0o, 0x. Por isso, precisamos fatiar a string
# retirando os dois primeiros digitos do resultado... por isso "[2:]".