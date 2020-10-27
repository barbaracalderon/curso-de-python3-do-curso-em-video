# Crie um programa que tenha uma tupla totalmente preenchida
# com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20)
# e mostrá-lo por extenso.
print('================== [NÚMERO POR EXTENSO] ==================')
while True:
    valor = int(input('Digite um valor entre 0 e 20: '))
    while valor < 0 or valor > 20:
        valor = int(input('Valor inválido. Digite um valor entre 0 e 20: '))
    tupla = (0, 'zero', 1, 'um', 2, 'dois', 3, 'três', 4, 'quatro', 5, 'cinco', 6, 'seis', 7, 'sete', 8, 'oito', 9, 'nove', 10, 'dez', 11, 'onze', 12, 'doze', 13, 'treze', 14, 'quatorze', 15, 'quinze', 16, 'dezesseis', 17, 'dezessete', 18, 'dezoito', 19, 'dezenove', 20, 'vinte')
    for c in tupla:
        if c == valor:
            posicao = valor * 2 + 1
            print(f'Você digitou {valor} e seu nome por extenso é {tupla[posicao]}.')
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        print('Saindo do programa. Volte sempre!')
        break

