# Crie um programa que tenha uma tupla totalmente preenchida
# com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20)
# e mostrá-lo por extenso.
print('================== [NÚMERO POR EXTENSO] ==================')
while True:
    valor = int(input('Digite um valor entre 0 e 20: '))
    while valor < 0 or valor > 20:
        valor = int(input('Valor inválido. Digite um valor entre 0 e 20: '))
    tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
             'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
             'dezessete', 'dezoito', 'dezenove', 'vinte')
    print(f'Você digitou {valor} e seu nome por extenso é {tupla[valor]}.')
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        print('Saindo do programa. Volte sempre!')
        break

