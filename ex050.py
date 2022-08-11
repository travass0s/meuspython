soma = 0
for n in range(0,6):
    p = int(input('Digite um número: '))
    if p % 2 == 0:
        soma += p
    else:
        print('Número ignorado!')
print('A soma dos números pares é {}'.format(soma))