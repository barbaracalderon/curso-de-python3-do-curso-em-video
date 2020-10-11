# Faça um programa que leia a largura e a altura de uma parede
# em metros, calcule sua área e a quantidade de tinta necessária
# para pintá-la, sabendo que cada litro de tinta, pinta uma área
# de 2 metros quadrados.

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura*altura
qtde_litros = area/2
print('A quantidade de litros de tinta necessária para pintar é: {}.'.format(qtde_litros))