anonasc = int(input('Ano de nascimento: '))
idade = 2022 - anonasc
if idade < 18:
    print('Ainda faltam {} anos'.format(18 - idade))
elif idade > 18:
    print('Você já deve ter se alistado há {} anos'.format(idade - 18))
else:
    print('Você deve se alistar este ano')