# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos dólares ela pode comprar.
# Considere:
# U$ 1.00 = R$ 3.27

valor_reais = float(input('Digite quanto dinheiro você tem na carteira: R$'))
qtde_dolar = valor_reais/3.27
print('Com R${:.2f} você consegue comprar U${:.2f}.'.format(valor_reais, qtde_dolar))