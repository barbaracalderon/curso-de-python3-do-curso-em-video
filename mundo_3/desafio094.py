# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa
# em um dicionário e todos os dicionários em uma lista. No final, mostre:
# a) Quantas pessoas foram cadastradas;
# b) A média de idade;
# c) Uma lista com as mulheres;
# d) Uma lista de pessoas com idade acima da média.
cont = soma_idade = 0
todos = []
mulheres = []
maiores = []
pessoa = {}
while True:
    pessoa["nome"] = str(input('Nome: '))
    while True:
        pessoa["sexo"] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa["sexo"] in 'MF':
            break
        print('Inválido! Digite novamente.')
    pessoa["idade"] = int(input('Idade: '))
    if pessoa["sexo"] in 'Ff':
        mulheres.append(pessoa["nome"])
    cont += 1
    soma_idade += pessoa["idade"]
    todos.append(pessoa.copy())
    pessoa.clear()
    while True:
        continuar = str(input('Quer cadastrar mais uma pessoa? [S/N]: ')).upper()[0]
        if continuar in 'SN':
            break
        print('Inválido. Apenas S ou N.')
    if continuar == 'N':
        break
media = soma_idade / cont
print('================ [RELATÓRIO] ==================')
print(f'Total de pessoas cadastradas: {cont}')
print(f'Média de idade: {media:.1f}')
print(f'Lista das mulheres cadastradas: {mulheres}')
for p in todos:
    if p["idade"] >= media:
        maiores.append(p["nome"])
print(f'Lista de pessoas com idade acima da média: {maiores}')
print('<< FIM >>')