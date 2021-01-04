# Desenvolva um programa que leia o primeiro termo e a razão de
# uma PA (Progressão Aritmética). No final, mostre os 10 primeiros
# termos dessa progressão.

print('=========== PROGRESSÃO ARITMÉTICA ===========')
primeiro = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão dessa PA: '))
decimo = primeiro + (10 - 1) * r
print('Os 10 primeiros termos dessa progressão são: ')
for i in range(primeiro, decimo + r, r):
    print(i, end= ' ')