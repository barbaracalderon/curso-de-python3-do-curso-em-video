# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens
# de até 200Km e R$0,45 para viagens mais longas.

distancia = float(input('Digite a distância da sua viagem em Km: '))
preco = 0
if distancia < 201:
    preco = distancia * 0.50
    print('O preço da passagem é: R$ {:.2f}'.format(preco))
else:
    preco = distancia * 0.45
    print('O preço da passagem é: R$ {:.2f}'.format(preco))