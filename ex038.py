n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('{} é maior que {}'.format(n1,n2))
elif n2 > n1:
    print('{} é maior que {}'.format(n2,n1))
else:
    print('O números digitados são iguais.')