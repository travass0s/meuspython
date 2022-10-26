qnt = 0
soma = 0
cancela = 0
while cancela == 0:
    n = int(input('Digite um número: (999 para cancelar) '))
    if (n == 999):
        cancela = 1
        print('Você digitou {} número(s) e a soma deles é {}'.format(qnt,soma))
        print('FIM')
    else:
        soma += n
        qnt += 1