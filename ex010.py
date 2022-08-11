real = float(input('Quanto dinheiro tem na carteira? '))
dolar = float(input('Quanto está a cotação do DÓLAR? '))
res = real / dolar
print('Seus R${:.2f} equivalem a US${:.2f} na cotação atual de {}'.format(real,res,dolar))