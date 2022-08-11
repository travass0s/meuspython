n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1+n2)/2
if media < 5:
    print('Reprovado com média {:.2f}'.format(media))
elif media > 5 and media < 7:
    print('Para recuperação com média {:.2f}'.format(media))
else:
    print('Aluno aprovado com média {}'.format(media))