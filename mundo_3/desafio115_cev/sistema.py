from mundo_3.desafio115_cev.lib.interface import *
from mundo_3.desafio115_cev.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if arquivoExiste(arq):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado.')
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Cadastro', 'Cadastrar Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        # Opção cadastrar uma nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print('<< SISTEMA ENCERRADO >>')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida do menu.\033[m')
    sleep(1)