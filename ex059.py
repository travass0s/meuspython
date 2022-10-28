print('Esta é a sua calculadora. Olá!')
print('Vamos começar com os valores, depois escolhemos a operação\nDurante o uso você pode alterar os valores, ok?')
f = 1
n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
while f == 1:
    print('\nOs valores são {} e {}, o que deseja fazer?'.format(n1,n2))
    print('[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Mostrar MAIOR\n[ 4 ] Alterar valores\n[ 5 ] Somar e aplicar desconto\n[ 6 ] Finalizar programa')
    m = int(input('Digite a opção: '))
    print('\n')
    if m == 1:
        print('A SOMA de {} e {} é: {}'.format(n1, n2, n1 + n2))
    elif m == 2:
        print('O PRODUTO entre {} e {} é: {}'.format(n1, n2, n1 * n2))
    elif m == 3:
        if n1 > n2:
            print('{} é maior que {}'.format(n1, n2))
            print('Primeiro valor é maior')
        else:
            print('{} é maior que {}'.format(n2, n1))
            print('Segundo valor é maior')
    elif m == 4:
        print('Atualmente os valores são {} e {}'.format(n1, n2))
        n1 = float(input('Altere primeiro valor para: '))
        n2 = float(input('Altere segundo valor para: '))
    elif m == 5:
        print('Primeiro informe qual percentual de desconto')
        percent = float(input('Percentual: '))
        desc = (n1+n2) * percent / 100
        total = (n1+n2) - desc
        print('Valor Total: {:.2f}\nValor com Desconto de {:.0f}: {:.2f}'.format(n1+n2, desc, total))
    elif m == 6:
        f = 0
print('O programa será finalizado. Obrigado.')
