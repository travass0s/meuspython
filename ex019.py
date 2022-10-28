import random
print('Vamos sortear o aluno vencedor!')
aluno1 = str(input('Digite o nome do Aluno 1: '))
aluno2 = str(input('Digite o nome do Aluno 2: '))
aluno3 = str(input('Digite o nome do Aluno 3: '))
aluno4 = str(input('Digite o nome do Aluno 4: '))
lista = [aluno1, aluno2, aluno3, aluno4]
sorteado = random.choice(lista)
print('O Aluno sorteado foi: {}'.format(sorteado))