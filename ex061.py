print('Gerador de PA')
n1 = int(input('Primeiro termo: '))
n= n1
r = int(input('Razão: '))
nx =  int(input('Termos: '))
f = nx
print('Mostrando PA de {} termos, começando de {} e com razão {}...'.format(nx, n1, r))
while f != 0:
    print('{} '.format(n), end='')
    n += r
    f = f - 1
