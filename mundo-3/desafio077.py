# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
tupla = ('cantar', 'brincar', 'cozinhar', 'estudar', 'trabalhar',
         'aprender', 'oceano', 'passeio', 'ferias', 'aprendizado')
for palavra in tupla:
    print(f'\nNa palavra {palavra.upper()} temos as vogais ', end='')
    for n in palavra:
        if n in 'aeiou':
            print(n.upper(), end='')