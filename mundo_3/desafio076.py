# Crie um programa que tenha uma tupla única com nomes de produtos e seus
# respectivos preços na sequência. No final, mostre uma listagem de preços
# organizando os dados em forma tabular.
tabela = ('Arroz', 2.75,
          'Feijão', 6.20,
          'Macarrão', 1.90,
          'Alface', 1.50,
          'Rúcula', 2.20,
          'Pasta de Dente', 2.00,
          'Detergente', 1.20,
          'Chocolate', 5.50,
          'Chips de Batata', 3.50,
          'Água com Gás', 1.05)
print(f'='*42)
print(f'{"TABELA DE PREÇOS [MERCADINHO SKINA]":^42}')
print(f'='*42)
for c in range(0, len(tabela)):
    if c % 2 == 0:
        print(f'{tabela[c]:.<35}', end='')
    else:
        print(f'R${tabela[c]:>5.2f}')
print(f'='*42)
print(f'{"Volte sempre!":^42}')