# Faça um programa que leia o nome completo de uma pessoa, mostrando
# em seguida o primeiro e o último nome separadamente.
# Exemplo:
# Ana Maria de Souza
# Primeiro: Ana
# Último: Souza

nome = str(input("Digite seu nome completo: ")).strip().split()
print("Seu primeiro nome: {}".format(nome[0]))
print("Seu último nome: {}".format(nome[len(nome)-1]))
