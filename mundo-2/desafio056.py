# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:
# i) A média de idade do grupo;
# ii) Qual é o nome do homem mais velho;
# iii) Quantas mulheres têm menos de 20 anos.

homem_velho = 0
soma_idade = 0
mulheres_novas = 0
for i in range(1, 5):
    print('\n ===== DADOS DA PESSOA {} ===== '.format(i))
    nome, idade, sexo = str(input('Nome: '.format(i))), int(input('Idade: '.format(i))), str(input('Sexo [H/M]: '.format(i))).lower()
    soma_idade = soma_idade + idade
    if sexo == 'homem' or sexo == 'h' or sexo == 'masculino':
        if idade > homem_velho:
            homem_velho = idade
            nome_velho = nome
    else:
        if idade < 20:
            mulheres_novas = mulheres_novas + 1
print('\n====================================')
print('Média de idade das pessoas: {} anos'.format(soma_idade/4))
print('O homem mais velho é {}.'.format(nome_velho))
print('Número de mulheres com menos de 20 anos: {}'.format(mulheres_novas))