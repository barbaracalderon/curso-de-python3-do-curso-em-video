# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma
# pessoa, retornando um valor literal indicando se uma pessoa tem o voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
def voto(nascimento):
    from datetime import date
    hoje = date.today().year
    idade = hoje - nascimento
    if idade >= 65:
        return print(f'Sua idade é {idade}. Seu voto é OPCIONAL.')
    elif idade >= 18:
        return print(f'Sua idade é {idade}. Seu voto é OBRIGATÓRIO.')
    elif idade >= 16:
        return print(f'Sua idade é {idade}. Seu voto é OPCIONAL.')
    else:
        return print(f'Sua idade é {idade}. Seu voto é NEGADO.')


# Programa Principal
nascimento = int(input('Digite seu ano de nascimento: '))
voto(nascimento)
