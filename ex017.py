import math
c1 = float(input('Digite o primeiro cateto: '))
c2 = float(input('Digite o segundo cateto: '))
print('='*10)
print('A Hipotenusa de {} e {} é {:.2f}'.format(c1,c2,math.hypot(c1,c2)))
