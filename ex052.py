print('\033[1mÉ PRIMO OU NÃO É??\033[m')
np = int(input('Qual número? '))
ate = np + 1
m = 0
for n in range(1,ate):
    if np % n == 0:
        print('\033[0:33m{}\033[m'.format(n), end=' ')
        m += 1
    else:
        print('\033[0:31m{}\033[m'.format(n), end=' ')
if m <= 2:
    print('\n{} divisores encontrados (!)'.format(m))
    print('\n{} é um número primo!'.format(np))
else:
    print('\n{} divisores encontrados'.format(m))
    print('\n{} NÃO é um número primo!'.format(np))
