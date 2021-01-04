from mundo_3.desafio115_cev.lib.interface import *
from time import sleep

while True:
    resposta = menu(['Cadastrar Pessoa', 'Ver Cadastro', 'Sair do Sistema'])
    if resposta == 1:
        print('CADASTRAR PESSOA')
    elif resposta == 2:
        print('VER CADASTRO')
    elif resposta == 3:
        print('<< SISTEMA ENCERRADO >>')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida do menu.\033[m')
    sleep(1)