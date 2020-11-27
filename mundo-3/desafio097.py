# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer
# como parâmetro e mostre a mensagem com tamanho adaptável.
def escreva(texto):
    print(f'~' * (len(texto) + 4))
    print(f'  {texto}')
    print(f'~' * (len(texto) + 4))


# Programa Principal
frase = str(input('Digite sua frase: '))
escreva(frase)
