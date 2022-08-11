import random
listanum = [0,1,2,3,4,5]
num = random.choice(listanum)
print('Bem vindo! Vamos brincar de adivinhação?')
print('Todos: VAAAAAAAAAAMOOOOOOOOOOOOOOOOS!')
n = int(input('Escolha um número entra 1 e 5: '))
if num == n:
    print('MUITO BEM! Você acertou!')
else:
    print('Você errou =( Tente novamente.')
print(n)
print(num)