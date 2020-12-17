import moeda
num = float(input('Digite o preço: R$'))
print(f'Aumentando 25% de {moeda.moeda(num)} temos o preço de {moeda.aumentar(num, 25, True)}')
print(f'Diminuindo 25% de {moeda.moeda(num)} temos o preço de {moeda.diminuir(num, 25, True)}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num, True)}')
print(f'A metade de {moeda.moeda(num)} é {moeda.metade(num, True)}')
# True significa que sim, quero a moeda com formatação
