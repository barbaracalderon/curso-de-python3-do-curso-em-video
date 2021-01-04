# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos
# e fechados na ordem correta.
expressao = str(input('Digite a sua expressão: '))
cont = cont_outro = 0
if '(' in expressao:
    for c in expressao:
        if c == '(':
            cont += 1
        if c == ')':
            cont_outro += 1
    if cont == cont_outro:
        print('Parabéns! Sua expressão está válida!')
    else:
        print('Sua expressão está inválida.')
else:
    print('Expressão não tem parênteses. Inválida.')