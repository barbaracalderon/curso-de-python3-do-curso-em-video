# Crie um programa que leia o nome de uma pessoa e diga
# se ela tem "SILVA" no nome.

nome = str(input("Digite o seu nome completo: ")).strip().lower()
if 'silva' in nome:
    resultado = 'Sim'
else:
    resultado = 'Não'
print("Esta pessoa tem 'Silva' no nome: {}.".format(resultado))