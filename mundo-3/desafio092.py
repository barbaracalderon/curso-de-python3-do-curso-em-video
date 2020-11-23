# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o
# (com idade) em um dicionário. Se por acaso a CTPS ("Carteira de Trabalho e Previdência
# Social") for diferente de ZERO, o dicionário receberá também o ano de contratação e o
# salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date, datetime
hoje = date.today().year
print('============== [DADOS DO TRABALHADOR] ================')
trabalhador = {}
trabalhador["Nome"] = str(input('Nome: '))
strnascimento = str(input('Ano de nascimento: '))
nascimento = datetime.strptime(strnascimento, '%Y').year # Converte str em data. O "Y" deixa 4 dígitos do ano.
trabalhador["Nascimento"] = nascimento
trabalhador["Idade"] = hoje - nascimento
trabalhador["CTPS"] = int(input('Nº da CTPS (Digite 0 se não tiver): '))
if trabalhador["CTPS"] != 0:
    strcontratacao = str(input('Ano de contratação: '))
    contratacao = datetime.strptime(strcontratacao, '%Y').year
    trabalhador["Contratação"] = contratacao
    trabalhador["Salário"] = float(input('Salário: R$ '))
    intaposentadoria = str(int(strcontratacao) + 35)
    aposentadoria = datetime.strptime(intaposentadoria, '%Y').year
    trabalhador["Aposentadoria"] = aposentadoria
    trabalhador["Idade que vai se aposentar"] = aposentadoria - nascimento
print(trabalhador)
print('============== [RELATÓRIO] ================')
for k, v in trabalhador.items():
    if k == 'CTPS' and v == 0:
        print(f'{k}: Não possui')
    else:
        print(f'{k}: {v}')
# Ficou comprido pelas conversões de string para o formato data.