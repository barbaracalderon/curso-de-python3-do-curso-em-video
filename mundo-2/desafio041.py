# A Confederação Nacional de Natação precisa de um programa que
# leia o ano de nascimento de um atleta e mostre sua categoria,
# de acordo com a idade:
# Até 09 anos: MIRIM;
# Até 14 anos: INFANTIL;
# Até 19 anos: JUNIOR;
# Até 20 anos: SÊNIOR;
# Acima: MASTER.

from datetime import date
hoje = date.today().year
nascimento = int(input('Digite o ano do seu nascimento: '))
tempo_vida = hoje - nascimento
if tempo_vida < 10:
    print('Sua categoria é MIRIM.')
elif tempo_vida < 15:
    print('Sua categoria é INFANTIL.')
elif tempo_vida < 20:
    print('Sua categoria é JUNIOR.')
elif tempo_vida < 21:
    print('Sua categoria é SÊNIOR.')
else:
    print('Sua categoria é MASTER.')