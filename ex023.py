n = input('Digite um número entre 1 e 9999: ')
num = '000' + n
print('Unidade: {}'.format(num[-1]))
print('Dezena: {}'.format(num[-2]))
print('Centena: {}'.format(num[-3]))
print('Milhar: {}'.format(num[-4]))

#num2 = int(num)
#print('Com matematica: ')
#print('Unidade: ', num2 % 10)
#print('Dezena: ', (num2 // 10) % 10)
#print('Centena ', (num2 // 100) % 10)
#print('Milhar ', (num2 // 1000) % 10)