anonasc = int(input('Ano de Nascimento: '))
idade = 2022 - anonasc
if idade <= 9:
    print('Idade MIRIM')
elif idade >= 10 and idade <= 14:
    print('Idade INFANTIL')
elif idade >= 15 and idade <= 19:
    print('Idade JUNIOR')
elif idade == 20:
    print('Idade SENIOR')
else:
    print('Idade MASTER')
print(idade)