n = 0
n = int(input('Quero consultar a tabuada de: '))
while n >= 0:
    print('Esta é a TABUADA de {}:'.format(n))
    for t in range(1,11):
        print('{} x {} = {}'.format(n,t,n*t))
    print('Para finalizar, digite um número negativo')
    n = int(input('Quero consultar a tabuada de: '))
print('TABUADA encerrado.')