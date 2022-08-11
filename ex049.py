n = int(input('Digite o número: '))
print('Tabuada para {}'.format(n))
for t in range(1,11):
    print('{} x {} = {}'.format(n,t,n*t))