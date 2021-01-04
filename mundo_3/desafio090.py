# Faça um programa que leia nome e média de um aluno, guardando também a situação
# em um dicionário. No final, mostre o conteúdo da estrutura na tela.
# PS: Considerei média 7.0
print('Vamos à situação do aluno! Considere média = 7.0')
dados = {}
dados["Nome"] = str(input('Nome do aluno: '))
dados["Média"] = float(input('Média: '))
if dados["Média"] > 7:
    dados["Situação"] = 'APROVADO'
elif dados["Média"] > 3:
    dados["Situação"] = 'RECUPERAÇÃO'
else:
    dados["Situação"] = 'REPROVADO'
print('=' * 25)
for k, v in dados.items():
    print(f'{k} é {v}')