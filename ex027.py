n = str(input('Digite seu nome: '))
nome = n.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Você tem {} nomes'.format(len(nome)))
print('Seu último nome é {}'.format(nome[len(nome)-1]))