# Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema
# de visualização de detalhes de aproveitamento de cada jogador.
print('======= [PLACAR DO JOGADOR] =========')
dados = {}
jogadores = []
gols = []
partidas = []
soma = 0
while True:
    dados.clear()
    dados["Jogador"] = str(input('Nome do jogador: '))
    total = int(input('Número de partidas jogadas: '))
    partidas.clear()
    for g in range(0, total):
        partidas.append(int(input(f'Gols na partida {g+1}: ')))
    dados["Gols"] = partidas[:]
    dados["Total de Gols"] = sum(partidas)
    jogadores.append(dados.copy())
    while True:
        continuar = str(input('Deseja continuar? [S/N]: ')).upper()[0]
        if continuar in 'SN':
            break
        print('Inválido. Digite S ou N.')
    if continuar == 'N':
        break
print('=========== RELATÓRIO ========================================')
print('<< DICIONÁRIO >>')
print(f'Lista "jogadores": {jogadores}')
print('<< TABELA >>')
print('Cód. ', end='')
for i in dados.keys():
    print(f'{i:<14}', end='')
print()
print('-------------------------------------------------------------')
for k, v in enumerate(jogadores):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<14}', end='')
    print()
print('=============================================================')
while True:
    codigo = int(input('Mostrar dados de qual jogador? Digite seu código (999 para encerrar): '))
    if codigo == 999:
        break
    if codigo >= len(jogadores):
        print(f'Inválido! Não existe jogador com este código {codigo}.')
    else:
        print(f'<< DADOS DO JOGADOR {jogadores[codigo]["Jogador"].upper()} >> ')
        for i, c in enumerate(jogadores[codigo]["Gols"]):
            print(f' -> No jogo {i+1} fez {g} gols.')
print('<< SISTEMA ENCERRADO >>')