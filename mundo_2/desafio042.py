# Refaça o DESAFIO035 dos triângulos, acrescentando o recurso de mostrar
# que tipo de triângulo será formado:
# EQUILÁTERO: todos os lados iguais;
# ISÓSCELES: dois lados iguais;
# ESCALENO: todos os lados diferentes.

a = float(input('Digite o lado A do triângulo: '))
b = float(input('Digite o lado B do triângulo: '))
c = float(input('Digite o lado C do triângulo: '))
if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print('Esses lados formam um triângulo EQUILÁTERO:\ntodos os lados são iguais.')
    elif a == b  or a == c or b == c:
        print('Esses lados formam um triângulo ISÓSCELES:\ndois lados são iguais.')
    else:
        print('Esses lados formam um triângulo ESCALENO:\ntodos os lados são diferentes.')    
else:
    print('Esses lados NÃO fazem um triângulo.')