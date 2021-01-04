# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# ----------------
# Abaixo de 18.5: Abaixo do Peso;
# Entre 18.5 e 25: Peso Ideal;
# 25 até 30: Sobrepeso;
# 30 até 40: Obesidade;
# Acima de 40: Obesidade Mórbida.
# ----------------

peso = float(input('Digite o seu peso em kilogramas: '))
altura = float(input('Digite a sua altura em metros: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Seu IMC é de {:.1f}. Situação: Abaixo do Peso.'.format(imc))
elif imc < 26:
    print('Seu IMC é de {:.1f}. Situação: Peso Ideal.'.format(imc))
elif imc < 31:
    print('Seu IMC é de {:.1f}. Situação: Sobrepeso.'.format(imc))
elif imc < 41:
    print('Seu IMC é de {:.1f}. Situação: Obesidade.'.format(imc))
else:
    print('Seu IMC é de {:.1f}. Situação: Obesidade Mórbida.'.format(imc))
