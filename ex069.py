cont = 'S'
mais18 = 0
homens = 0
mulheres20 = 0
print('Vamos cadastrar PESSOAS!')
while cont == 'S':
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')).upper()

    idade = int(input('Digite a idade: '))

    if sexo == 'M':
        print('\nDetectamos uma pessoa do sexo MASCULINO com {} anos'.format(idade))
        homens += 1
    elif sexo == 'F':
        print('\nDetactamos uma pessoa do sexo FEMININO com {} anos'.format(idade))
        if idade > 20: mulheres20 += 1

    if idade > 18: mais18 += 1

    cont = ' '
    while cont not in 'SN':
        cont = str(input('\nDeseja cadastrar mais pessoas [S/N]? ')).upper()
print('\nResultado do cadastro:\nMaiores de 18 anos: {}\nHomens: {}\nMulheres com mais de 20 anos: {}'.format(mais18,homens,mulheres20))