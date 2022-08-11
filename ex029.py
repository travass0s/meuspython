print('Você saber se você foi multado e quando você deve, taokey?')
vel = int(input('A qual velocidade estava quando passou por Goiana? '))
velo = (vel-80)*7
if velo < 0:
    print('Você estava dentro do limite de velocidade')
    print('Muito bem :D')
else:
    print('Você estava {}km/h além do limite de velocidade'.format(vel-80))
    print('Sua Multa é de R${}'.format(velo))
    print('Boleto pode ser pago através do Banco do Brasil ou CEF')
    print('Vencimento em 28/08/2022')