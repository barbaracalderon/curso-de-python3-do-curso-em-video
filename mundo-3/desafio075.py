# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final, mostre:
# a) Quantas vezes apareceu o valor 9;
# b) Em que posição foi digitado o primeiro valor 3;
# c) Quais foram os números pares.
print('================== [04 NÚMEROS] ==================')
tupla = (int(input('Digite o 1ª valor: ')),
         int(input('Digite o 2ª valor: ')),
         int(input('Digite o 3ª valor: ')),
         int(input('Digite o 4ª valor: ')))
cont_posicao = posicao_tres = 0
pares = []
for c in tupla:
    cont_posicao += 1
    if c == 3:
        posicao_tres = cont_posicao
    elif c % 2 == 0:
        pares.append(c)
print('-------------------------------------------------')
print('RELATÓRIO')
print(f'Os valores que você forneceu foram: {tupla}')
print(f'O número 9 apareceu {tupla.count(9)} vezes')
print(f'O número 3 apareceu primeiro na {posicao_tres}ª posição')
print(f'Os números pares são: {pares}')