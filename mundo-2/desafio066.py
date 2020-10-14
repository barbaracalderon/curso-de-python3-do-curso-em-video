# Crie um programa que leia números inteiros pelo teclado. O programa só vai parar
# quando o usuário digitar o valor 999, que é a condição de parada. No final,
# mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando
# o flag).
contador = soma = 0
print('========== SOMA DE VALORES ==========')
while True:
    num = int(input('Digite um valor inteiro (ou "999" para parar): '))
    if num == 999:
        break
    contador += 1
    soma += num
print(f'Você digitou {contador} valores. A soma deles é {soma}.')