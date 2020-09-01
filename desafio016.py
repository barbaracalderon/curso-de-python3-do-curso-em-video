# Crie um programa que leia um número real qualquer pelo teclado e
# mostre na tela a sua porção inteira.
# Exemplo:
# Digite um número: 6.127
# O número 6.127 tem a parte inteira 6.

num_real = float(input("Digite um número: "))
num_inteiro = int(num_real)
print("O número {} tem a parte inteira {:.0f}.".format(num_real, num_inteiro))