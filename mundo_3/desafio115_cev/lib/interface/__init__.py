def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuário escolheu não digitar uma opção.\033[m')
            return 0
        else:
            return n

def linha(tam=40):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(40))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    cont = 1
    for item in lista:
        print(f'\033[33m{cont}\033[m: \033[30m{item}\033[m')
        cont += 1
    print(linha())
    opcao = leiaInt('\033[33mDigite sua opção: \033[m')
    return opcao