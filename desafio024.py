# Crie um programa que leia o nome de uma cidade
# e diga se ela começa ou não com o nome "SANTO".

cidade = input("Digite o nome de uma cidade: ")
cidade_quebra = cidade.split()
primeiro_nome = cidade_quebra[0]

if primeiro_nome == 'Santo' or primeiro_nome == 'santo' or primeiro_nome == 'SANTO':
    resultado = 'sim'
else:
    resultado = 'nao'
print("O primeiro nome da cidade {} começa com o nome 'Santo'.".format(resultado))