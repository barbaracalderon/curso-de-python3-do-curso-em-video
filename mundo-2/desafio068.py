# Faça um programa que jogue par ou ímpar com o computador. O jogo
# só será interrompido quando o jogador perder, mostrando o total de
# vitórias consecutivas que ele conquistou no final do jogo.
import random
comp = random.randint(1,10)
print('========== [O JOGO DO PAR OU ÍMPAR] ==========')
cont = cont_jogos = soma = jog_num = comp = 0
soma = jog_num + comp
while True:
    jog_num = int(input('Digite um valor inteiro: '))
    jog = str(input('Par ou Ímpar? [P/I]: ').upper().strip())[0]
    while jog not in 'PpIi':
        jog = str(input('Par ou Ímpar? [P/I]: ').upper().strip())[0]
    cont_jogos += 1
    if jog == 'P':
        if soma % 2 == 0:
            print('Parabéns! Você GANHOU!')
            cont += 1
        else:
            print('Fim da linha! Você PERDEU.')
            break
    elif jog == 'I':
        if soma % 2 == 0:
            print('Fim da linha! Você PERDEU.')
            break
        else:
            print('Parabéns! Você GANHOU!')
            cont += 1
print('='*45)
print(f'RELATÓRIO\nTotal de Partidas: {cont_jogos}\nVitórias: {cont}\nVolte sempre!')
print('='*45)
