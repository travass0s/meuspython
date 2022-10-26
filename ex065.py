soma = 0
qnt = 0
cnt = 's'
while cnt == 's':
    n = int(input('Digite um número: '))
    if qnt == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    soma += n
    qnt += 1
    cnt = str(input('Deseja continuar? [S/N] '))
print('Você digitou {} números e média foi {:.2f}'.format(qnt,soma/qnt))
print('O Maior foi {} e o menor foi {}'.format(maior,menor))