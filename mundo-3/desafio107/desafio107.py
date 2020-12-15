# Crie um módulo chamado moeda.py que tenham as funções incorporadas aumentar(), diminuir(),
# dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
import moeda
num = float(input('Digite o preço: R$'))
print(f'Aumentando 25% de R${num} temos o preço de R${moeda.aumentar(num)}')
print(f'Diminuindo 25% de R${num} temos o preço de R${moeda.diminuir(num)}')
print(f'O dobro de R${num} é R${moeda.dobro(num)}')
print(f'A metade de R${num} é R${moeda.metade(num)}')
