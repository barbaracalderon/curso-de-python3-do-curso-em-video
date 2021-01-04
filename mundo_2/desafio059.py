# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
escolha = 0
while escolha != 5:
    print( """\n------- OPERAÇÕES -------\n
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa\n""")
    escolha = int(input('Escolha uma das opções acima: '))
    if escolha == 1:
        resultado = a + b
        print('Operação escolhida: {}\nValores escolhidos: {} e {}\nResultado: {}'.format(escolha, a, b, resultado))
    elif escolha == 2:
        resultado = a * b
        print('Operação escolhida: {}\nValores escolhidos: {} e {}\nResultado: {}'.format(escolha, a, b, resultado))
    elif escolha == 3:
        if a > b:
            resultado = a
            print('Operação escolhida: {}\nValores escolhidos: {} e {}\nResultado: {}'.format(escolha, a, b, resultado))
        elif b > a:
            resultado = b
            print('Operação escolhida: {}\nValores escolhidos: {} e {}\nResultado: {}'.format(escolha, a, b, resultado))
        else:
            resultado = 'empate'
            print('Operação escolhida: {}\nValores escolhidos: {} e {}\nResultado: {}'.format(escolha, a, b, resultado))
    elif escolha == 4:
        a = int(input('Digite o primeiro valor: '))
        b = int(input('Digite o segundo valor: '))
    elif escolha == 5:
        print('Saindo do programa...')
    else:
        print('Opção inválida. Tente novamente!')
print('Programa finalizado com sucesso. Você saiu.')
