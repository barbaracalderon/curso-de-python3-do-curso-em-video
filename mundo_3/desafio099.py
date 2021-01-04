# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com
# valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
def maior(*val):
    for n in val:
        print('-' * 38)
        print(f'O maior valor é {max(val[0])}')
        print('-' * 38)
        print('<< ENCERRADO >>')


# Programa Principal
valores = []
print('=========== [MAIOR VALOR] ============')
while True:
    valor = int(input('Valor inteiro: '))
    valores.append(valor)
    continuar = str(input('Continuar? [S/N]: ')).upper()[0]
    while continuar not in 'SN':
        print('Comando inválido.')
        continuar = str(input('Continuar? [S/N]: ')).upper()[0]
    if continuar == 'N':
        break
print(f'Os valores digitados foram {valores}')
maior(valores)
