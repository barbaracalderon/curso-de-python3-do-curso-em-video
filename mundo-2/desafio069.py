# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa
# cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# a) Quantas pessoas têm mais de 18 anos;
# b) Quantos homens foram cadastrados;
# c) Quantas mulheres têm menos de 20 anos.
maior_idade = qtde_homens = qtde_mulheres_jovens = 0
print('================== [CADASTRO DE PESSOAS] ==================')
while True:
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]
    if idade > 18:
        maior_idade += 1
    if sexo == 'M':
        qtde_homens += 1
    else:
        if idade < 21:
            qtde_mulheres_jovens += 1
    continuar = str(input('Você deseja cadastrar mais pessoas? [S/N]: ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Você deseja cadastrar mais pessoas? [S/N]: ')).upper().strip()[0]
    if continuar in 'N':
        break
print('='*45)
print(f'[RELATÓRIO]\nQuantidade de pessoas com mais de 18 anos: {maior_idade}\nQuantidade de homens cadastrados: {qtde_homens}\nQuantidade de mulheres com menos de 20 anos: {qtde_mulheres_jovens}')