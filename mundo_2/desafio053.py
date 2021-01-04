# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

print('====================== É PALÍNDROMO? ======================')
frase = str(input('Digite a sua frase (sem acentos ou cedilhas): ')).replace(' ', '').lower()
frase_contrario = frase[::-1]
if frase == frase_contrario:
    print('A frase é um palíndromo!')
else:
    print('A frase não é um palíndromo.')