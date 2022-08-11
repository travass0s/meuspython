n1 =  int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
r = n1 % n2
e = n1 ** n2
print('Você digitou {} e {}'.format(n1,n2))
print('A soma é {}, multiplicando fica {}'.format(s,m))
print('Dividindo fica {:.3f}, e inteira é {} e o resto é {}'.format(d,di,r))
print('{} elevado a {} fica {}'.format(n1,n2,e))