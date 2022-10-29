from random import randint
n1 = randint(1, 20)
maior = n1
menor = n1
n2 = randint(1, 20)
if n2 < menor:
    menor = n2
if n2 > maior:
    maior = n2
n3 = randint(1, 20)
if n3 < menor:
    menor = n3
if n3 > maior:
    maior = n3
n4 = randint(1, 20)
if n4 < menor:
    menor = n4
if n4 > maior:
    maior = n4
n5 = randint(1, 20)
if n5 < menor:
    menor = n5
if n5 > maior:
    maior = n5
nums = n1, n2, n3, n4, n5
print(nums)
print(f'O maior número é {maior} e o menor é {menor}')