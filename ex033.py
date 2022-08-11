print('MAIOR e MENOR')
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o último valor: '))
lista = [n1, n2, n3]
print('Baseado nos valores informados, temos:')
print('O MAIOR valor é: {}'.format(max(lista)))
print('O MENOR valor é: {}'.format(min(lista)))
print('Você informou {} valores'.format(len(lista)))
