# FUNÇÕES =========================================
def cadastrar_pessoa():
    nome = validaNome()
    return nome

def validaNum(esc=0):
    while True:
        try:
            if esc in (1, 2, 3):
                print(f'Ok, escolha {esc} validada')
                return esc
            else:
                esc = int(input('\033[31mDigite um valor válido.\033[m\nDigite opção: '))
        except (TypeError, ValueError):
            print('\033[31mERRO! Opção inexistente.\033[m')


def validaNome(nom=''):
    while True:
        nom = str(input('\033[33mDigite o nome da pessoa\033[m: '))
        try:
            if nom.isalpha():
                print(f'Aqui é o nome {nom} depois de validado. Deu ok.')
                return nom
            else:
                print('\033[31mERRO! O nome deve conter apenas letras.\033[m')
        except (TypeError, ValueError):
            print('\033[31mERRO! Opção inexistente.\033[m')
            num = str(input('\033[33mDigite o nome da pessoa\033[m: '))
            continue


# JANELAS ========================================

def janela_cadastrar():
    cabecalho('Cadastrar Nova Pessoa')
    while True:
        cadastro.append(cadastrar_pessoa())
        continuar = str(input('Cadastrar outra pessoa? [S/N]: ')).upper().strip()
        if continuar not in 'SN':
            print('\033[31mTente de novo.\033[m')
        elif continuar == 'N':
            break
    return 0

def janela_ver():
    cabecalho('Ver Pessoas Cadastradas')
    if len(cadastro) == 0:
        print('\033[31mNão há ninguém cadastrado.\033[m')
        while True:
            voltar = str(input('\033[33mDigite 0 para retornar\033[m: ')).strip()
            if voltar.isnumeric() and voltar == '0':
                voltar = int(voltar)
                return voltar
            else:
                print('\033[31mTente de novo.\033[m')
    else:
        for i in range(len(cadastro)):
            print(f'{i + 1}', end='')
            print(f'    {cadastro[i]}')
        print('-' * 35)
        while True:
            voltar = str(input('\033[33mDigite 0 para retornar\033[m: ')).strip()
            if voltar.isnumeric() and voltar == '0':
                voltar = int(voltar)
                return voltar
            else:
                print('\033[31mTente de novo.\033[m')

def janela_sair():
    print('-' * 35)
    print('\033[31m<< SISTEMA ENCERRADO >>\033[m')

def escolha_janelas(janela):
        if janela == 1:
            janela_cadastrar()
        if janela == 2:
            janela_ver()
        if janela == 3:
            janela_sair()

# MENUS ================================================
def cabecalho(msg):
    print('=' * 35)
    print(f'\033[32m{msg.upper().center(35)}\033[m')
    print('-' * 35)

def opcoes_principal():
    print('\033[33m1\033[m: Cadastrar Nova Pessoa')
    print('\033[33m2\033[m: Ver Pessoas Cadastradas')
    print('\033[33m3\033[m: \033[31mSair do Sistema\033[m')
    print('-' * 35)
    opcao = int(input('Digite sua opção: '))
    opcao_final = validaNum(opcao)
    return opcao_final

def menu(n=0):
    cabecalho('Menu do Sistema')
    escolha = opcoes_principal()
    opcao = validaNum(escolha)
    return opcao

# PRINCIPAL =============================================
janela = opcao = escolha = 0
cadastro = []
janela = menu()
while True:
    if janela == 0:
        janela = menu()
    if janela == 1:
        janela = janela_cadastrar()
    elif janela == 2:
        janela = janela_ver()
    elif janela == 3:
        janela = janela_sair()
        break