# Escreva um programa para aprovar o empréstimo bancário para a compra
# de uma casa. O programa vai perguntar o valor da casa, o salário do
# comprador e em quantos anos ele vai pagar.
#
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder
# 30% do salário ou então o empréstimo será negado.

casa = float(input('Digite o valor da casa que deseja comprar: R$ '))
salario = float(input('Digite o valor do salário do comprador: R$ '))
anos = int(input('Digite a quantidade de anos que deseja pagar: '))
prestacao = casa / (anos*12)

if prestacao > salario * 0.3:
    print('Sentimos muito. A prestação mensal excedeu 30% do salário (R$ {:.2f}) e, por isso, foi negada.'.format(prestacao))
else:
    print('Parabéns! Seu empréstimo foi aprovado. O valor da prestação mensal é de R$ {:.2f}'.format(prestacao))