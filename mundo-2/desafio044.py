# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# À vista dinheiro/cheque: 10% de desconto;
# À vista no cartão: 5% de desconto;
# Em até 2x no cartão: preço normal;
# Em 3x ou mais no cartão: 20% de juros.

preco = float(input('Digite o valor do produto: R$ '))
cartao_dinheiro = int(input('Digite:\n[1] para pagamento DINHEIRO/CHEQUE (à vista)\n[2] para pagamento EM CARTÃO\nOpção Escolhida: '))
if cartao_dinheiro == 1:
    preco_final = preco * 0.90
    print('Seu desconto é de 10%! O valor final a ser pago é de: R$ {}'.format(preco_final))
elif cartao_dinheiro == 2:
    vezes = int(input('Seu pagamento é em CARTÃO. Digite:\n[3] para pagamento À VISTA\n[4] para pagamento PARCELADO 2x\n[5] para pagamento PARCELADO 3x (ou mais)\nOpção Escolhida: '))
    if vezes == 3:
        preco_final = preco * 0.95
        print('Seu desconto é de 5%! O valor final a ser pago é de: R$ {}'.format(preco_final))
    elif vezes == 4:
        preco_final = preco
        print('O valor final a ser pago é de: R$ {}'.format(preco_final))
    elif vezes == 5:
        preco_final = preco * 1.20
        print('Sua compra tem juros! O valor final a ser pago é de: R$ {}'.format(preco_final))
    else:
        print('Essa opção não existe. Tente novamente.')
else:
    print('Opção Inválida de pagamento. Tente novamente.')