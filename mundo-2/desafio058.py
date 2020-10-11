# Melhor o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
# palpites foram necessŕios para vencer.
import random
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num_escolhido = random.choice(num)
num_usuario = int(input('Escolha um número entre 0 e 10: '))
contador = 0
while num_usuario != num_escolhido:
    print('Ainda não foi. Vamos de novo!')
    num_usuario = int(input('Escolha um número entre 0 e 10: '))
    contador += 1
print('Parabéns! Você acertou o número que eu pensei: {}\nPara isso, você tentou {} vezes. Nessa última, você acertou!'.format(num_escolhido, contador))