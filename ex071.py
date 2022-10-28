import time

print('=' * 30)
print('{:^30}'.format('BANQ e SAQ'))
print('=' * 30)
print('Cédulas disponíveis: R$5, R$10, R$20 e R$50\nEscolha um valor múltiplo de 5')
valor = int(input('Quanto você quer sacar? R$'))
total = valor
print('Processando...')
time.sleep(2)
print('Verificando saldo...')
time.sleep(1)
print('Seu saldo será feito da seguinte forma:')
if valor / 50 >= 1:
    print('{:.0f} cédulas de 50 Reais'.format(valor/50))
    valor = valor % 50
    #print(valor)
    #if valor > 0: print('E sobrou {:.0f} Reais'.format(valor))
if valor / 20 >= 1:
    print('{:.0f} cédulas de 20 Reais'.format(valor/20))
    valor = valor % 20
    #print(valor)
    #if valor > 0: print('E sobrou {:.0f} Reais'.format(valor))
if valor / 10 >= 1:
    print('{:.0f} cédulas de 10 Reais'.format(valor/10))
    valor = valor % 10
    #print(valor)
    #if valor > 0: print('E sobrou {:.0f} Reais'.format(valor))
if valor / 5 >= 1:
    print('{:.0f} cédulas de 5 Reais'.format(valor/5))
    valor = valor % 5
    #print(valor)
    #if valor > 0: print('E sobrou {:.0f} Reais')
if valor != 0: print('Não é possível sacar {:.0f} Reais'.format(valor))
cont = ' '
while cont not in 'SN':
    cont = str(input('\nDeseja concluir o saque deste modo [S/N]? ')).upper()
if cont == 'S': print('\nSaque concluído. Confira do dinheiro.')
else: print('Saque cancelado.')