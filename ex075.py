pares = 0
n1 = int(input('Digite um valor: '))
if (n1 % 2) == 0:
    pares += 1
n2 = int(input('Digite o segundo valor: '))
if (n2 % 2) == 0:
    pares += 1
n3 = int(input('Digite o terceiro valor: '))
if (n3 % 2) == 0:
    pares += 1
n4 = int(input('Digite o último valor: '))
if (n4 % 2) == 0:
    pares += 1
nums = n1, n2, n3, n4
if nums.count(9) > 0: print(f'O número 9 aparece {nums.count(9)} vezes')
else: print('O número 9 não foi digitado')
if nums.count(3) != 0: print(f'O número 3 aparece na posição {nums.index(3)+1}')
else: print('O número 3 não foi digitado')
print(f'Foram digitados {pares} números pares')