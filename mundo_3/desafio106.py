# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual
# vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.
c = ('\033[m',        # 0 - sem cor
     '\033[0;30;41m',   # 1 - vermelho
     '\033[0;30;42m',   # 2 - verde
     '\033[0;30;43m',   # 3 - amarelo
     '\033[0;30;44m',   # 4 - azul
     '\033[0;30;45m',   # 5 - roxo
     '\033[7;30m'       # 6 - branco
     )


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 5)
    print(c[6], end='')
    help(com)
    print(c[0], end='')


def titulo(msg, cor=0):
    tam = len(msg) + 6
    print(c[cor], end='')
    print('=' * tam)
    print(f'   {msg}')
    print('=' * tam)
    print(c[0], end='')


# Programa Principal
while True:
    titulo('[SISTEMA DE AJUDA: PyHELP]', 2)
    print(f'\033[94m(Digite "FIM" para sair)\033[m ')
    comando = str(input('\033[94mDigite o comando:\033[m ')).strip().lower()
    if comando == 'fim':
        break
    else:
        ajuda(comando)
titulo('<< PROGRAMA ENCERRADO >>', 1)
