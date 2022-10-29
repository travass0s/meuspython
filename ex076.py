bd = ('Pão', 2, 'Bolacha', 3.50, 'Trigo', 5.50, 'Leite', 4, 'Ovos', 15, 'Creme de Leite', 4)
print('-' * 40)
print(f'{"ESCOLHA O SEU PRODUTO":^40}')
print('-' * 40)
for i in range(0, len(bd),2):
    print(f'{bd[i]:.<30} R${bd[i+1]:>7.2f}')
print('-' * 40)
print(f'{"(C) PARA COMPRA (V) PARA VENDER":^40}')
print('-' * 40)