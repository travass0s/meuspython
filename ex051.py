print('GERADOR DE PA')
n1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
for pa in range(0,10):
    print('{} '.format(n1), end='- ')
    n1 += r
print('Acabou')
