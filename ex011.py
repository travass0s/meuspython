print('Utilize as medidas em METROS')
altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede? '))
area = altura * largura
print('Você vai precisar de {:.2f} litros de tinta \npara pintar esta parede de {:.2f}m²'.format((area/2),area))