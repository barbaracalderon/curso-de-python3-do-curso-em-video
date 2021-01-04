# Melhore o DESAFIO061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos.
print('=========== PROGRESSÃO ARITMÉTICA ===========')
primeiro = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão dessa PA: '))
termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print('{}, '.format(termo), end='')
        termo = termo + r
        contador = contador + 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')