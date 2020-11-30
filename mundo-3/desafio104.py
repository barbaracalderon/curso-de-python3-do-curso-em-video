# Crie um programa que tenha a função leiaInt(), que vai funcionar semelhante à função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico. Exemplo: n = leiaInt('Digite um n: ')
def leiaInt(mens):
    mens = str(input('Digite um valor: '))
    while True:
        if mens.isnumeric():
            mens = int(mens)
            break
        else:
            print('Inválido! Digite um valor numérico.')
            mens = str(input('Digite um valor: '))
    print(f'{mens} é um número.')


# Programa Principal
mens = leiaInt('Digite um valor: ')
