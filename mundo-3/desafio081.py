# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# a) Quantos números foram digitados;
# b) A lista de valores ordenada de forma decrescente;
# c) Se o valor 5 foi digitado e está ou não na lista.
lista = []
cont = 0
while True:
    num = int(input('Digite um valor: '))
    continuar = str(input('Deseja continuar? [S/N]: ')).upper()[0]
    cont += 1
    lista.append(num)
    if continuar == 'N':
        lista.sort(reverse=True)
        break
print('=============== [RELATÓRIO] =================')
print(f'A lista ordenada de forma decrescente é: {lista}')
print(f'Foram digitados {cont} números.')
if 5 in lista:
    print('O valor 5 está presente na lista.')
else:
    print('O valor 5 não está na lista.')