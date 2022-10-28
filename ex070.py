import time
from time import sleep

itens = 0
itens1000 = 0
total = 0
menor = 0
maior = 0
mbarato = ' '

print('INICIANDO UMA NOVA VENDA...')
time.sleep(3)
cont = 'S'
while cont == 'S':
    produto = str(input('\nDigite o nome do produto: '))
    valor = float(input('Digite o valor em REAIS: '))
    if total == 0:
        menor = valor
        maior = valor
        mbarato = produto
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
            mbarato = produto
    itens += 1
    total += valor
    print('\nValor Total: R${:.2f}\n{} itens registrados'.format(total,itens))
    if valor > 1000: itens1000 += 1
    time.sleep(1)
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Adicionar mais produtos [S/N]? ')).upper()
print('\nCompra finalizada!')
print('\nDetalhes:\nTotal: R${:.2f}\n{} itens acima de R$1000\n{} é o item mais barato custando R${:.2f}'.format(total,itens1000,mbarato,menor))