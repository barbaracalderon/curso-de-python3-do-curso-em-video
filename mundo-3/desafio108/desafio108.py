# Crie um módulo chamado moeda.py que tenham as funções incorporadas aumentar(), diminuir(),
# dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
import moeda
num = float(input('Digite o preço: R$'))
moe = moeda.formato(num)
aum = moeda.aumentar(num)
dim = moeda.diminuir(num)
dob = moeda.dobro(num)
met = moeda.metade(num)
print(f'Aumentando 25% de {moe} temos o preço de {moeda.formato(aum)}')
print(f'Diminuindo 25% de {moe} temos o preço de {moeda.formato(dim)}')
print(f'O dobro de {moe} é {moeda.formato(dob)}')
print(f'A metade de {moe} é {moeda.formato(met)}')
