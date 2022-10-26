t = int(input('Quantos termos? '))
n = 1
while n < t:
    if n == 1:
        n1 = 0
        n2 = 1
        print('{} - {} - '.format(n1,n2), end='')
        n += 1
    else:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        print('{} - '.format(n3), end='')
        n += 1
        if n == t:
            print('FIM')