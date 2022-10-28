c = 1
a = 0
import random
listanum = [0,1,2,3,4,5,6,7,8,9,10]
print('Bem vindo! Vamos brincar de adivinhação?')
print('Todos: VAAAAAAAAAAMOOOOOOOOOOOOOOOOS!')
while c < 2:
    num = random.choice(listanum)
    n = int(input('\nEscolha um número entra 1 e 10:'))
    if num == n:
        a += 1
        if a == 1:
            print('MUITO BEM! Você acertou de PRIMEIRA!!')
        else:
            print('MUITO BEM! Você acertou em {} tentativas!'.format(a))
        c = 2
    else:
        print('Você errou =( Tente novamente.')
        a += 1