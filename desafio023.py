# Faça um programa que leia um número de 0 a 9999 e mostre na tela
# cada um dos dígitos separados.
# Exemplo:
# Digite um número: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

numero = input("Digite um número entre 0 e 9999: ")

if len(numero) == 4:
    unidade = numero[3]
    dezena = numero[2]
    centena = numero[1]
    milhar = numero[0]
    print("Unidade: {}.".format(unidade))
    print("Unidade: {}.".format(dezena))
    print("Unidade: {}.".format(centena))
    print("Unidade: {}.".format(milhar))
elif len(numero) == 3:
    unidade = numero[2]
    dezena = numero[1]
    centena = numero[0]
    milhar = 0
    print("Unidade: {}.".format(unidade))
    print("Unidade: {}.".format(dezena))
    print("Unidade: {}.".format(centena))
    print("Unidade: {}.".format(milhar))
elif len(numero) == 2:
    unidade = numero[1]
    dezena = numero[0]
    centena = 0
    dezena = 0
    print("Unidade: {}.".format(unidade))
    print("Unidade: {}.".format(dezena))
    print("Unidade: {}.".format(centena))
    print("Unidade: {}.".format(milhar))
elif len(numero) == 1:
    unidade = numero[0]
    dezena = 0
    centena = 0
    milhar = 0
    print("Unidade: {}.".format(unidade))
    print("Unidade: {}.".format(dezena))
    print("Unidade: {}.".format(centena))
    print("Unidade: {}.".format(milhar))