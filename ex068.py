from random import randint
print('Vamos jogar PAR ou ÍMPAR')
print('O jogo só acaba quando o jogador perder. Boa sorte!')
ganhou = 0
vic = 0
while ganhou == 0:
    jog = int(input('[1] ÍMPAR\n[2] PAR\nEscolha...: '))
    if jog != 1 and jog != 2: break
    n = int(input('Digite um número entre 1 e 5: '))
    if n < 1 or n > 5: break
    cpu = randint(1,5)
    print('Você jogou {}'.format(jog))
    print('CPU jogou {}'.format(cpu))
    total = n+cpu
    if total % 2 == 0:
        res = 2
        print('{} é PAR!'.format(total))
    else:
        res = 1
        print('{} é ÍMPAR!'.format(total))
    if res == jog:
        print('Você ganhou!\n\nEscolha novamente')
        vic += 1
    else:
        print('Você perdeu!\n')
        ganhou = 1
if vic == 0:
    print('Perdeu com 0 vitórias...')
else:
    print('Perdeu com {} vitórias...'.format(vic))