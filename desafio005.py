# Faça um programa que leia um número inteiro e mostre na tela o seu
# sucessor e seu antecessor.

numero = int(input('Digite um número: '))
suce = numero+1
ante = numero-1
print('O sucessor desse número é {} e o antecessor é {}.'.format(suce, ante))
