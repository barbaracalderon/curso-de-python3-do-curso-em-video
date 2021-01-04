# Reescreva a função leiaInt() que fizemos no Desafio 104, incluindo agora a possibilidade da digitação
# de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (TypeError, ValueError):
            print('\033[31mERRO! Digite um valor inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mVocê escolheu não digitar nenhum número.\033[m')
            return 0
        else:
            return n

def leiaFloat(val):
    while True:
        try:
            b = float(input(val))
        except (TypeError, ValueError):
            print('\033[31mERRO! Digite um valor real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mVocê escolheu não digitar nenhum número.\033[m')
            return 0
        else:
            return b

valor = leiaInt('Digite um valor inteiro: ')
num = leiaFloat('Digite um valor real: ')
print(f'O valor inteiro digitado foi {valor} e o valor real foi {num}')