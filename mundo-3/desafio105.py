# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
# com as seguintes informações:
# a) Quantidade de notas;
# b) A maior nota;
# c) A menor nota;
# d) A média da turma;
# e) A situação (opcional).
def notas():
    turma["Quantidade de Notas"] = len(boletim)
    turma["Maior Nota"] = max(boletim)
    turma["Menor Nota"] = min(boletim)
    turma["Média"] = soma/len(boletim)
    while True:
        while True:
            opcional = str(input('Deseja ver a situação da turma? [S/N]: ')).upper()[0]
            if opcional in 'SN':
                break
            print('Inválido. Tente novamente.')
        if opcional == 'N':
            break
        else:
            if turma["Média"] > 3:
                turma["Situação"] = 'TURMA EM RECUPERAÇÃO'
                break
            elif turma["Média"] >= 7:
                turma["Situação"] = 'TURMA APROVADA!'
                break
            else:
                turma["Situação"] = 'TURMA REPROVADA'
                break
    return print(turma)


# Programa Principal
boletim = []
turma = {}
soma = media = 0
while True:
    nota = float(input('Digite uma nota: '))
    soma += nota
    boletim.append(nota)
    while True:
        continuar = str(input('Deseja adicionar mais uma nota? [S/N]: ')).upper()[0]
        if continuar in 'SN':
            break
        print('Inválido. Tente novamente.')
    if continuar == 'N':
        break
notas()