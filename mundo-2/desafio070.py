# Crie um programa que leia o nome e o preço de vários produtos. O programa
# deverá perguntar se o usuário vai continuar. No final, mostre:
# a) Qual é o total gasto na compra;
# b) Quantos produtos custam mais de R$1000;
# c) Qual é o nome do produto mais barato.
print('============== [MERCADINHO SKINA] ===============')
print('Bem-vindo ao Mercadinho Skina! Vamos calcular suas compras.')
total_compras = contador_mil = mais_barato = 0
nome_mais_barato = ''
nome_produto = str(input('Digite o nome do produto: ')).strip()
preco_produto = float(input('Digite o valor do produto: R$ '))
mais_barato = preco_produto
nome_mais_barato = nome_produto
continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()
if continuar == 'S':
    while True:
        total_compras += preco_produto
        if preco_produto > 1000:
            contador_mil += 1
        if preco_produto < mais_barato:
            nome_mais_barato = nome_produto
            mais_barato = preco_produto
        if continuar == 'N':
            break
        nome_produto = str(input('Digite o nome do produto: ')).strip()
        preco_produto = float(input('Digite o valor do produto: R$ '))
        continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()
print('==================================================')
print(f'[RELATÓRIO]\nTotal da Compra: R${total_compras:.2f}\nQuantidade de produtos que custa mais de R$1000: {contador_mil}\nProduto mais barato: {nome_mais_barato}')
print('==================================================')
