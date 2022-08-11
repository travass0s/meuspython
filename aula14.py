n = 1
pares = 0
impares = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        pares += 1
        print('Número PAR detectado!')
    else:
        impares += 1
        print('Número IMPAR detectado!')
pares = pares - 1
print('Você digitou:\n{} números pares e\n{} números ímpares'.format(pares,impares))