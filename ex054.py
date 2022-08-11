mais = 0
menos = 0
for g in range(0,7):
    ano = int(input('Digite o ano de nascimento da pessoa {}: '.format(g+1)))
    if 2022 - ano >= 21:
        mais += 1
        print('Pessoa com {} anos. Adicionado ({})'.format(2022-ano,mais))
    else:
        menos += 1
        print('Pessoa com {} anos. Adicionado ({})'.format(2022-ano,menos))
print('Total de pessoas:\nMaiores de idade: {}\nMenores de idade: {}'.format(mais,menos))