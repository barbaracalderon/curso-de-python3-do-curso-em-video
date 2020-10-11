# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final de acordo com a média atingida:
# a) Média abaixo de 5.0: REPROVADO;
# b) Média entre 5.0 e 6.9: RECUPERAÇÃO;
# c) Média 7.0 ou superior: APROVADO.

nota_a = float(input('Digite sua primeira nota: '))
nota_b = float(input('Digite sua segunda nota: '))
media = (nota_a + nota_b)/2
if media < 5.0:
    print('Sua média é de {:.1f}\nSituação: REPROVADO.'.format(media))
elif media < 7.0:
    print('Sua média é de {:.1f}\nSituação: RECUPERAÇÃO.'.format(media))
else:
    print('Sua média é de {:.1f}\nSituação: APROVADO.'.format(media))
