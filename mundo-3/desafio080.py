# Crie um programa onde o usuário possa digitar cinco valores numéricos e
# cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.
lista = []
for c in range (0, 5):
    a = int(input('Digite um valor: '))
    if c == 0 or a > lista[-1]:
        lista.append(a)
    else:
        posicao = 0
        while posicao < len(lista):
            if a <= lista[posicao]:
                lista.insert(posicao, a)
                break
            posicao += 1
print('============================================')
print(f'A lista ordenada é {lista}')