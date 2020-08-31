# Faça um algoritmo que leia o salário de um funcionário e mostre
# seu novo salário, com 15% de aumento.

salario = float(input('Digite o seu salário: R$ '))
novo_salario = salario*1.15
print('Seu salário de R$ {:.2f} recebeu 15% de aumento. Agora você ganha RS {:.2f}'.format(salario, novo_salario))