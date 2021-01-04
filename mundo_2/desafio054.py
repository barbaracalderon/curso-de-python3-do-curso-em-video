# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade
# e quantas já são maiores.

from datetime import date
hoje = date.today().year # Aloca para 'hoje' o ano atual (sempre atualizado automaticamente)
maiores = 0
menores = 0
for i in range(1, 8):
    nascimento = int(input('Digite a data de nascimento da pessoa {}: '.format(i)))
    if hoje - nascimento > 17:
        maiores += 1
    else:
        menores += 1
print('Número de pessoas maiores de idade: {}\nNúmero de pessoas menores de idade: {}'.format(maiores, menores))
