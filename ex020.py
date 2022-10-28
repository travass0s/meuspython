from random import shuffle
aluno1 = str(input('Digite o nome do aluno 1: '))
aluno2 = str(input('Digite o nome do aluno 2: '))
aluno3 = str(input('Digite o nome do aluno 3: '))
aluno4 = str(input('Digite o nome do aluno 4: '))
lista = [aluno1,aluno2,aluno3,aluno4]
print('Embaralhando...')
shuffle(lista)
print('A ordem para apagar o quadro é:')
print(lista)
