import math
angulo = float(input('Digite o ângulo para calcular: '))
radiano = math.radians(angulo)
print('Dados para o angulo {}°:'.format(angulo))
print('Também conhecido como {} radianos'.format(radiano))
print('Seno: {:.2f}'.format(math.sin(radiano)))
print('Cosseno: {:.2f}'.format(math.cos(radiano)))
print('Tangente: {:.2f}'.format(math.tan(radiano)))