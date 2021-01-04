# Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
# mostre a média entre todos os valores e qual foi o maior e o menor valor lido.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
soma = contador = 0
continuar = 'S'
print('========== DADOS DE VALORES INTEIROS =========')
num = int(input('Digite um valor inteiro: '))
maior = num
menor = num
while continuar == 'S':
    soma += num
    contador += 1
    media = soma/contador
    if num >= maior:
        maior = num
    if num <= menor:
        menor = num
    continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if continuar == 'S':
        num = int(input('Digite um valor inteiro: '))
print('Você digitou {} números. Estes são os dados:\nMédia Total: {}\nMaior número digitado: {}\nMenor número digitado: {}'.format(contador, media, maior, menor))