preco = float(input('Qual o valor do produto? '))
desc = (preco * 5) / 100
print('O Produto que custa R${:.2f}'.format(preco))
print('Ficará por R${:.2f} com R${:.2f} de desconto'.format(preco-desc,desc))