# Faça um algoritmo que leia o preço de um produto
# e motre seu novo preço, com 5% de desconto.

preco_prod = float(input('Digite o preço do produto: R$ '))
novo_preco = preco_prod*0.95
print('Estamos dando 5% de desconto nos produtos. O novo preço, com desconto, é: R$ {:.2f}.'.format(novo_preco))