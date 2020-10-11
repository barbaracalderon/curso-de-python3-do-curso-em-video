# Faça um programa que leia o ano de nascimento de um jovem
# e informe, de acordo com a sua idade:
# a) Se ele ainda vai se alistar ao serviço militar;
# b) Se é a hora de se alistar;
# c) Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta
# ou que passou do prazo.

from datetime import date
hoje = date.today().year
ano_nascimento = int(input('Digite o ano em que você nasceu: '))
limite = ano_nascimento + 18
if limite == hoje:
    print('É a hora de se alistar!')
elif limite < hoje:
    print('Você já passou do tempo de alistamento faz {} anos.'.format(hoje-limite))
else:
    print('Aguarde seu tempo. Você vai se alistar em {} anos.'.format(limite-hoje))