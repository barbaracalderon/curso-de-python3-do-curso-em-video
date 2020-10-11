# O mesmo professor do desafio anterior (desafio019) quer sortear a ordem de apresentação
# de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a
# ordem sorteada.

import random
a = input("Digite o nome do primeiro aluno: ")
b = input("Digite o nome do segundo aluno: ")
c = input("Digite o nome do terceiro aluno: ")
d = input("Digite o nome do quarto aluno: ")

lista = [a, b, c, d]

escolhido_1 = random.choice(lista)
lista.remove(escolhido_1)
escolhido_2 = random.choice(lista)
lista.remove(escolhido_2)
escolhido_3 = random.choice(lista)
lista.remove(escolhido_3)
escolhido_4 = random.choice(lista)

print("A ordem sorteada dos alunos foi: {}, {}, {} e {}.".format(escolhido_1, escolhido_2, escolhido_3, escolhido_4))
