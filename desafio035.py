# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.

a = float(input('Digite o lado A do triângulo: '))
b = float(input('Digite o lado B do triângulo: '))
c = float(input('Digite o lado C do triângulo: '))
if a < b + c and b < a + c and c < a + b:
    print('Esses lados fazem um triângulo!')
else:
    print('Esses lados NÃO fazem um triângulo.')