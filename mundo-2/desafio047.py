# Crie um programa que mostre na tela todos os números pares
# que estão no intervalo entre 1 e 50.

print('Estes são os números pares entre 1 e 50:')
for i in range(2, 51, 2): # O segundo "2" significa que está "pulando de dois em dois"
    print(i, end=' ')