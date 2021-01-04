# Faça um programa que tenha uma função chamada área(), que receba as dimensões
# de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def area(l, c):
    area = l * c
    print('-------------------- CÁLCULO --------------------')
    print(f'Cálculo de {l}m x {c}m = área de {area:.2f}m²')


# Programa Principal
print('================ ÁREA DE TERRENO =================')
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)
