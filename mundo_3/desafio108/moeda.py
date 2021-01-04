def aumentar(n):
    r = n * 1.25
    return r

def diminuir(n):
    r = n * 0.75
    return r

def dobro(n):
    r = n * 2
    return r

def metade(n):
    r = n / 2
    return r

def formato(n=0, moeda='R$'):
    return f'{moeda}{n:>5.2f}'.replace('.', ',')