# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o seu salário: '))
aumento = 0
salario_novo = 0
if salario > 1250:
    aumento = salario * 0.1
    salario_novo = salario + aumento
    print('Seu novo salário é R$ {:.2f} e o seu aumento foi de R$ {:.2f}'.format(salario_novo, aumento))
else:
    aumento = salario * 0.15
    salario_novo = salario + aumento
    print('Seu novo salário é R$ {:.2f} e o seu aumento foi de R$ {:.2f}'.format(salario_novo, aumento))
    