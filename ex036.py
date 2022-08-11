valorcasa = float(input('Valor do imóvel: '))
valorsal = float(input('Valor do salário: '))
valorms = 12*(int(input('Anos para pagar: ')))
parcela = valorcasa / valorms
parcelamaxima = valorsal * 30 / 100
print(valorms)
print(valorsal)
print(valorcasa)
print(parcela)
print(parcelamaxima)
if parcela < parcelamaxima:
    print('Emprestimo liberado!')
else:
    print('Empréstimo negado!')