distkm = float(input('Digite a distância (km) até seu destino: '))
if distkm >= 200:
    taxa = 0.45
else:
    taxa = 0.50
print('Calculando o valor da sua passagem...')
print('Para sua viagem de {}km: R${}'.format(distkm,distkm*taxa))