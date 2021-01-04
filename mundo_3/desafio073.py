# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
# do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois, mostre:
# a) Apenas os 5 primeiros colocados;
# b) Os últimos 4 colocados da tabela;
# c) Uma lista com os times em ordem alfabética;
# e) Em que posição na tabela está o time da Chapecoense.
# Obs.: Hoje é 27 de outubro de 2020.
brasileirao = ('Internacional', 'Flamengo', 'Atlético-MG', 'Fluminense', 'São Paulo',
               'Santos', 'Palmeiras', 'Fortaleza', 'Grêmio', 'Ceará SC', 'Atlético-GO',
               'Sport Recife', 'Corinthians', 'Bahia', 'Bragantino-SP', 'Botafogo',
               'Vasco da Gama', 'Athletico-PR', 'Coritiba', 'Goiás')
posicao = 0
mensagem = ''
for c in brasileirao:
    if c == 'Chapecoense':
        posicao = c + 1
    if posicao == 0:
        mensagem = ', este time não está na série A!'
print('================= [BRASILEIRÃO - SÉRIE A] ==================')
print('De acordo com a Tabela de Classificação (do dia 27/10/2020):')
print(f'5 PRIMEIROS COLOCADOS:\n{brasileirao[:5]}')
print('------------------------------------------------------------')
print(f'OS ÚLTIMOS 4 COLOCADOS (LANTERNINHAS):\n{brasileirao[-4:]}')
print('------------------------------------------------------------')
print(f'LISTA EM ORDEM ALFABÉTICA:\n{sorted(brasileirao)}')
print('------------------------------------------------------------')
print(f'POSIÇÃO DA CHAPECOENSE NA TABELA: {posicao}{mensagem}')