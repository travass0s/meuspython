print('Qual é o seu aumento?')
sal = float(input('Qual o seu salário atual? '))
if sal >= 1250:
    taxa = 10
else:
    taxa = 15
print('De acordo com o salário informando')
print('Seu aumento é de {}%'.format(taxa))
print('Seu salário será de R${:.2f}'.format(sal + (sal * taxa / 100)))