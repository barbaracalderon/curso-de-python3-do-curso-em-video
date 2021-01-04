# Escreva um programa que pergunte a quantidade de Km percorridos por
# um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e
# R$0,15 por Km rodado.

qtde_km = float(input('Digite a quantidade de KM rodados: '))
qtde_dias = float(input('Digite a quantidade de dias que o carro foi alugado: '))
preco = (qtde_km*0.15)+(qtde_dias*60)
print('O carro andou {:.2f}KM e ficou alugado por {:.0f} dias. O preço total do aluguel é de R$ {:.2f}.'.format(qtde_km, qtde_dias, preco))