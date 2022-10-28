print('Gerador de PA')
n1 = int(input('Primeiro termo: '))
n= n1
r = int(input('Razão: '))
nx = int(input('Termos: '))
f = nx
nx2 = nx
print('Mostrando PA de {} termos, começando de {} e com razão {}...'.format(nx, n1, r))
while nx != 0:
    while f != 0:
        print('{} '.format(n), end='')
        n += r
        f = f - 1
    print('\nMostrar mais termos?\n[ 0 ] Para finalizar')
    nx = int(input('Digite: '))
    f = nx
    nx2 += nx
print('Programa finalizado. Você mostrou {} termos'.format(nx2))