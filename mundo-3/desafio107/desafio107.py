# Crie um módulo chamado moeda.py que tenham as funções incorporadas aumentar(), diminuir(),
# dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
import moeda
num = int(input('Digite o valor da moeda: '))
aum = moeda.aumentar(num)
dim = moeda.diminuir(num)
dob = moeda.dobro(num)
met = moeda.metade(num)
print(f'O valor da moeda é {num}\nQuando aumentada tem seu valor {aum}\nQuando diminuída tem valor {dim}\nSeu dobro é {dob}\nSua metade é {met}')
