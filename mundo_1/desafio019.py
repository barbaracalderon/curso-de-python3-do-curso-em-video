# Um professor quer sortear um dos seus quatro alunos para
# apagar o quadro. Faça um programa que ajude ele, lendo
# o nome deles e escrevendo o nome do escolhido.

import random
a = str(input("Digite o nome do primeiro aluno: "))
b = str(input("Digite o nome do segundo aluno: "))
c = str(input("Digite o nome do terceiro aluno: "))
d = str(input("Digite o nome do quarto aluno: "))

lista = [a, b, c, d]
escolhido = random.choice(lista)

print("O aluno escolhido foi {}.".format(escolhido))