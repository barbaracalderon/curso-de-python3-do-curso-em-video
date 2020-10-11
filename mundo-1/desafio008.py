# Escreva um programa que leia um valor em metros e o exiba
# convertido em centímetros e milímetros.

valor_metros = float(input('Digite um valor em metros: '))
valor_cent = valor_metros*100
valor_mili = valor_metros*1000
print('Esse valor é {:.0f}cm e {:.0f}mm.'.format(valor_cent, valor_mili))