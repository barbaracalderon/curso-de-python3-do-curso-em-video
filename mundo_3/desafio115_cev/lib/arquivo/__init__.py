from mundo_3.desafio115_cev.lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        #'rt' = read and text
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        #'wt+' = write, text and if not existing... then create a file
        a.close()
    except:
        print('Houve um erro na criação do arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        print(a.read())
