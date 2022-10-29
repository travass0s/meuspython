serieb = ('Cruzeiro', 'Grêmio', 'Bahia', 'Vasco', 'Ituano', 'Sport', 'Sampaio Corrêa', 'Londrina', 'Criciúma', 'CRB', 'Guarani', 'Ponte Preta', 'Vila Nova', 'Tombense', 'Chapecoense', 'CSA', 'Novorizontino', 'Brusque', 'Operário-PR', 'Náutico')

print('Listando...')
print(f'Os CINCO PRIMEIROS: {serieb[0:5]}')
print(f'Os QUATRO ÚLTIMOS: {serieb[-4:]}')
print(f'Todos os times em ordem alfabética: {sorted(serieb)}')
print(f'A posição do CHAPECOENSE: {serieb.index("Chapecoense")+1}')