# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma
# lista composta. No final, mostre um boletim contendo a média de cada um e permita
# que o usuário possa mostrar as notas de cada aluno individualmente.
tabela = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    continuar = str(input('Deseja continuar? [S/N]: ')).upper()[0]
    media = (nota1 + nota2)/2
    tabela.append([nome, [nota1, nota2], media])
    if continuar == 'N':
        break
print('-----------------------')
print(f'{"N.":<4}{"NOME":>8}{"MÉDIA":>6}')
print('-----------------------')
for i, a in enumerate(tabela):
    print(f'{i:<4}{a[0]:>8}{a[2]:>6.2f}')
print('-----------------------')
while True:
    opcao = int(input('Deseja ver as notas de qual aluno? Escolha pelo número (999 interrompe): '))
    if opcao == 999:
        break
    if opcao <= len(tabela) - 1:
        print(f'As notas do aluno {tabela[opcao][0]} são {tabela[opcao][1]}')