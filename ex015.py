print('\033[4;34mSistema de Aluguel de Veículos\033[m')
km = float(input('Digite quantos Kilometros percorreu: '))
dias = int(input('Digite a quantidade de dias de utilização: '))
usokm = km * 0.15
usodias = dias * 60
total = usokm + usodias
print('\033[0;34mTotal da Cobrança:\033[m')
print('Com {}km percorridos: \033[0;33mR${:.2f}\033[m'.format(km, usokm))
print('Com {} dias utilizados: \033[0;33mR${:.2f}\033[m'.format(dias,usodias))
print('Total de \033[1:31mR${:.2f}\033[m'.format(total))