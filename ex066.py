n = 0
qnt = 0
soma = 0
while n != 999:
    n = int(input('Digite um número ou digite 999 para terminar: '))
    if n == 999: break
    soma += n
    qnt += 1
print('Você digitou {} números e somando fica {}'.format(qnt,soma))