# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique
# o número a calcular; e outro chamado show, que será um valor lógido (opcional) indicando se será mostrado
# ou não na tela o processo de cálculo do fatorial.
def fatorial(num=1, show=0):
    """
    -> Calcula o fatorial de um número qualquer.
    :param num: O número a ser calculado o fatorial.
    :param show: Mostrar ou não o cálculo (Opcional).
    :return: O valor do fatorial do número Num.
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(f' = {f}\n', end='')
        f *= c
    return f


# Programa Principal
num = int(input('Digite um número: '))
while True:
    show = input('Mostrar a conta? [S/N]: ').upper()[0]
    if show == 'S':
        show = True
        break
    elif show == 'N':
        show = False
        break
    else:
        print('Código inválido. Digite "True" ou "False".')
fatorial(num, show)
print(f'O fatorial de {num} é {fatorial(num)}')
