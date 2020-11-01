# Crie um programa onde o usuário possa digitar vários valores numéricos e
# cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
lista = []
while True:
    valor = int(input('Digite um valor: '))
    if valor in lista:
        print('O valor já existe na lista!')
        pass
    elif valor not in lista:
        lista.append(valor)
        print('O valor foi adicionado.')
    continuar = str(input('Continuar? [S/N]: ')).upper().strip()
    while continuar not in 'SN':
        print('Valor inválido. Tente novamente.')
        continuar = str(input('Continuar? [S/N]: ')).upper().strip()
    if continuar == 'N':
        break
print(f'Os valores digitados, em ordem crescente, é {lista}')