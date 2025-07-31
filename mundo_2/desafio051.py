# Desenvolva um programa que leia o primeiro termo e a razão de
# uma PA (Progressão Aritmética). No final, mostre os 10 primeiros
# termos dessa progressão.

print('=========== PROGRESSÃO ARITMÉTICA ===========')
primeiro = float(input('Digite o primeiro termo: '))
r = float(input('Digite a razão dessa PA: '))
print('Os 10 primeiros termos dessa progressão são: ')
for i in range(10):
    print(f'{primeiro:.0f}', end=' -> ')
    primeiro += r
