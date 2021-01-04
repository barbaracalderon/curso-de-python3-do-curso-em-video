# Crie um programa que faça o computador jogar "JOKENPÔ" com você.
# PS: "Jokenpô" é o jogo do pedra-papel-tesoura.

import random
usuario = str(input('Escolha sua arma!\nDigite "P" (pedra), "PA" (papel) ou "T" (tesoura): ')).lower()
opcao = ['p', 'pa', 't']
computador = random.choice(opcao)
if usuario == 'p':
    if computador == 'p':
        print('Você escolheu pedra e eu também! Empatamos.')
    elif computador == 'pa':
        print('Você escolheu pedra e eu papel! Você perdeu.')
    elif computador == 't':
        print('Você escolheu pedra e eu tesoura! Você GANHOU!')
elif usuario == 'pa':
    if computador == 'p':
        print('Você escolheu papel e eu pedra! Você GANHOU!')
    elif computador == 'pa':
        print('Você escolheu papel e eu também! Empatamos.')
    elif computador == 't':
        print('Você escolheu papel e eu tesoura! Você perdeu.')
elif usuario == 't':
    if computador == 'p':
        print('Você escolheu tesoura e eu pedra! Você perdeu.')
    if computador == 'pa':
        print('Você escolheu tesoura e eu papel! Você GANHOU!')
    if computador == 't':
        print('Você escolheu tesoura e eu também! Empatamos.')
else:
    print('Letra inválida. Só podemos jogar com aquelas letras indicadas.')