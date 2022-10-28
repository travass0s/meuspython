from time import sleep
print('FATORIAL!')
n = int(input('Digite um número inteiro: '))
nf = n
f = n - 1
print('Calculando {}!...\n'.format(n))
while f != 0:
    nf = nf * f
    f = f - 1
sleep(1)
print('{}! = {}'.format(n,nf))