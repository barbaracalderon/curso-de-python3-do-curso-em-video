# Crie um programa que leia o nome completo de uma pessoa e mostre:
# a) O nome com todas as letras maiúsculas;
# b) O nome com todas minúsculas;
# c) Quantas letras ao todo (sem considerar espaços);
# d) Quantas letras tem o primeiro nome.

nome = input("Digite o seu nome completo: ")
nome_mai = nome.upper()
nome_min = nome.lower()
nome_sem = nome.replace(" ", "")
letras = len(nome_sem)
nome_quebrado = nome.split()
primeiro_nome = nome_quebrado[0]
count = 0
for i in primeiro_nome:
    count = count+1

print("O nome com todas as letras maiúsculas: {}.".format(nome_mai))
print("O nome com todas as letras minúsculas: {}.".format(nome_min))
print("O nome tem {} letras ao todo.".format(letras))
print("O primeiro nome tem {} letras.".format(count))