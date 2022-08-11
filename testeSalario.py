from time import sleep
print('\033[1;34mVAMOS CALCULAR SEU SALÁRIO DO MÊS!\033[m')
q = 541.60
sb1 = float(input('Digite o valor do seu \033[1;36msalário:\033[m '))
print('\nAgora vamos iniciar com algumas informações básicas:')
print('Seu salário é de \033[1;36mR${:.2f}\033[m'.format(sb1))
print('\033[1mINSS\033[m: 9% ({})'.format(sb1 * 8 / 100))
print('\033[1mVale Transporte\033[m: 6% ({})'.format(sb1 * 6 / 100))
sb = sb1 - (sb1 * 8 / 100) - (sb1 * 9 /100)
#print('Calculando...')
#sleep(1)
print('Pegamos seu salário e reduzimos as taxas acima.\nSeu Salário Base é de \033[1:mR${:.2f}\033[m\n'.format(sb))
cota = float(input('Quando você vendeu? R$'))
mes = float(input('Qual a cota do mês? R$'))
porcentu = cota / mes
cotinha = 0
print('\n\033[1mSeu Relatório:\033[m')
#sleep(1)
print('=' * 35)
if porcentu > 1:
    cotinha = cotinha + 0.5
    cotinha = cotinha + (porcentu - 1)
    sb = sb + (sb * cotinha) - q
    print('Você vendeu cota + \033[1:30:42m{:.2f}%\033[m este mês'.format((porcentu*100)-100))
    print('Você vai receber \033[1mR${:.2f}\033[m'.format(sb))
elif porcentu > 0.7 and porcentu < 1:
    cotinha = cotinha + 0.25
    sb = sb + (sb * cotinha) - q
    print('Você vendeu \033[1:30:43m{:.2f}%\033[m da cota este mês'.format(porcentu * 100))
    print('Faltou \033[1mR${:.2f}\033[m para alcançar a cota de 100%'.format(mes-cota))
    print('Você vai receber \033[1mR${:.2f}\033[m'.format(sb))
else:
    sb = sb - q
    print('Você vendeu \033[1:30:41m{:.2f}\033[m de cota este mês'.format(porcentu))
    print('Faltou \033[1mR${:.2f}\033[m para alcançar a cota de 100%'.format(mes-cota))
    print('Você vai receber \033[1mR${:.2f}\033[m'.format(sb))

print('Você recebeu quinzena de \033[1m{:.2f}\033[m'.format(q))
print('=' * 35)
print('\n\033[1m~Os valores apresentados aqui são apenas para referência~\033[m')
#print(cotinha)
#print(sb)
#print(porcentu)
