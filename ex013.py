print('Parabéns! Você ganhou um aumento de 15%!')
salario = float(input('Digite o valor atual do seu salário: R$'))
aumento = salario * 15 / 100
novosal = salario + aumento
print('Pronto! Seu salário era de R${:.2f}'.format(salario))
print('Agora será de R${:.2f}'.format(novosal))
print('Um aumento de R${:.2f}'.format(aumento))
print('Parabéns, gafanhoto!')

