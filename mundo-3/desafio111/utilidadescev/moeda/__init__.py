def aumentar(preco=0, taxa=0, formato=False):
    r = preco + (preco * taxa/100)
    return r if formato is False else moeda(r)

def diminuir(preco=0, taxa=0, formato=False):
    r = preco - (preco * taxa/100)
    return r if formato is False else moeda(r)

def dobro(preco=0, formato=False):
    r = preco * 2
    return r if formato is False else moeda(r)

def metade(preco=0, formato=False):
    r = preco / 2
    return r if formato is False else moeda(r)

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>5.2f}'.replace('.', ',')

def resumo(preco=0, taxa=10, taxared=5):
    print('=' * 30)
    print('CÁLCULO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço Original: \t{moeda(preco)}')
    print(f'Metade do Preço: \t{metade(preco, True)}')
    print(f'Dobro do Preço: \t{dobro(preco, True)}')
    print(f'{taxa}% de Aumento: \t{aumentar(preco, taxa, True)}')
    print(f'{taxared}% de Aumento: \t\t{diminuir(preco, taxared, True)}')
    print('=' * 30)