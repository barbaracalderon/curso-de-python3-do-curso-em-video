# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Digite a velocidade do carro em Km/h: '))
km = 0
custo = 0
if velocidade > 80:
    print('Você foi multado!')
    custo = (velocidade - 80) * 7
    print('Sua multa é de: R$ {:.2f}'.format(custo))
else:
    print('Muito bem! Você está dentro do limite de velocidade.')