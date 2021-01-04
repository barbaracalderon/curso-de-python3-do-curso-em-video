# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex.
# 5! = 5 x 4 x 3 x 2 x 1
# 5! = 120
numero = int(input('Digite um número: '))
resultado = numero
diminuidor = numero - 1
if numero == 0:
    resultado = 1
else:
    while diminuidor > 0:
        resultado = resultado * diminuidor
        diminuidor -= 1
print('O fatorial do número {} é {}'.format(numero, resultado))
