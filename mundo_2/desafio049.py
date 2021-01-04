# Refaça o desafio009, mostrando a tabuada de um número que o usuário escolher,
# só que agora usando o laço for.

numero = int(input('TABUADA DE UM NÚMERO\nDigite um número inteiro: '))
print('================================\n========= TABUADA DO {} ========= '.format(numero))
for i in range(0,11):
    resultado = numero * i
    print('{} x {:2} = {:2}'.format(numero, i, resultado))