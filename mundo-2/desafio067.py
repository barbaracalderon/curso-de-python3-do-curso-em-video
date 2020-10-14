# Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário. O programa será interrompido quando
# o número solicitado for negativo.
print('========== TABUADA ==========')
while True:
    num = int(input('Digite um valor para ver sua tabuada: '))
    if num < 0:
        break
    for i in range(0,11):
        resultado = num * i
        print(f'{num} x {i} = {resultado}')
print('Chegamos ao fim. Você saiu do programa. Até a próxima!')