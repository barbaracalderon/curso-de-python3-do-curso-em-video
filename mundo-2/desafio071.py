# Crie um programa que simule o funcionamento de um caixa eletrônico. No início,
# pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa
# vai informar quantas cédulas de cada valor serão entregues.
# OBS.: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print('=============== [BANCO SKINA - CAIXA ELETRÔNICO] ==============')
print('Bem-vindo ao Caixa Eletrônico do Banco Skina! Estamos na sua Conta Corrente.')
print('Temos as seguintes cédulas disponíveis: R$50,00; R$20,00; R$10,00 e R$1,00')
valor = int(input('Digite o valor a ser sacado: R$ '))
total = valor
cedula = 50
total_cedula = 0
while True:
    if total >= cedula:
        total -= cedula
        total_cedula += 1
    else:
        print(f'Total de {total_cedula} cédulas de R$ {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedula = 0
        if total == 0:
            break
print('=' * 63)
print('Volte sempre! O Banco Skina agradece.')