# Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema
# de visualização de detalhes de aproveitamento de cada jogador.
print('======= [PLACAR DO JOGADOR] =========')
dados = {}
jogadores = []
gols = []
soma = 0
while True:
    dados.clear()
    dados["Jogador"] = str(input('Nome do jogador: '))
    dados["Partidas"] = int(input('Número de partidas jogadas: '))
    for g in range(0, dados["Partidas"]):
        gol = int(input(f'Gols na partida {g+1}: '))
        gols.append(gol)
        dados["Gols"] = gols[:]
    dados["Total de Gols"] = sum(gols)
    while True:
        continuar = str(input('Deseja continuar? [S/N]: ')).upper()[0]
        if continuar in 'SN':
            break
        print('Inválido. Digite S ou N.')
    jogadores.append(dados.copy())
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
print()