# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do
# jogador e quantas partidas ele jogou. Depois, vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos no campeonato.
print('======= [PLACAR DO JOGADOR] =========')
dados = {}
dados["Jogador"] = str(input('Nome do jogador: '))
dados["Partidas"] = int(input('Número de partidas jogadas: '))
gols = []
soma = 0
for g in range(0, dados["Partidas"]):
    gol = int(input(f'Gols na partida {g+1}: '))
    gols.append(gol)
dados["Gols"] = gols[:]
dados["Total de Gols"] = sum(gols)
print('=========== RELATÓRIO =============')
print('<< DICIONÁRIO >> ==================')
print(dados)
print('<< CAMPOS >> ======================')
for k, v in dados.items():
    print(f'O campo {k} tem valor {v}')
print('<< RESUMO DA PARTIDA >> ===========')
print(f'O jogador {dados["Jogador"]} jogou {dados["Partidas"]} partidas!')
for a in range(0, dados["Partidas"]):
    print(f'Na partida {a+1} fez {dados["Gols"][a]} gols')
print('<< TODOS OS DADOS >> =============')
for k, v in dados.items():
    print(f'{k}: {v}')