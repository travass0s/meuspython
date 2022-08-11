print('Vamos descobrir se o ano é BISSEXTO')
print('Utilize sempre no formato 1xxx ou 2xxx, com 4 dígitos')
ano = int(input('Digite um ano com 4 dígitos: '))
if ano % 4 == 0:
    print('O ano {} é BISSEXTO! a'.format(ano))
else:
    #checar se é divisível por 100 e 400
    if ano % 100 == 0:
        if ano % 400 == 0:
            print('O ano {} é BISSEXTO! x'.format(ano))
        else:
            print('O ano {} NÃO é BISSEXTO! z'.format(ano))
    else:
        print('O ano {} NÃO é BISSEXTO! y'.format(ano))
print(ano % 4)