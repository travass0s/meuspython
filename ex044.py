print('\033[1:32mMÓDULO DE COMPRA\033[m')
valor = float(input('Valor do produto: '))
print('\033[1mFormas de Pagamento:\033[m \n1- Dinheiro/Pix\n2- Crédito à vista\n3- Crédito 2x\n4- Crédito 3x ou mais')
formapg = int(input('Digite: '))
if formapg == 1:
    print('\033[1:32mPagamento em Dinheiro/Pix\033[m\nValor com Desconto: \033[1:31mR${:.2f}\033[m'.format(valor - (valor * 10 / 100)))
elif formapg == 2:
    print('\033[1:32mPagamento em Crédito à vista\033[m\nValor com Desconto: \033[1:31mR${:.2f}\033[m'.format(valor - (valor * 5 / 100)))
elif formapg == 3:
    print('\033[1:32mPagamento em Crédito 2x\033[m\nNão é permitido desconto nesta modalidade de pagamento\nValor do produto: \033[1:31mR${:.2f}\033[m'.format(valor))
elif formapg == 4:
    print(
        '\033[1:32mPagamento em Crédito 3x ou mais\033[m\nTaxa de 20% para esta modalidade de pagamento\nValor do produto: \033[1:31mR${:.2f}\033[m'.format(valor + (valor * 20 / 100)))
print('Finalize sua compra direto no Caixa.\nObrigado.')