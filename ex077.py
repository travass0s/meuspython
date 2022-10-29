palavras = ('Florianopolis', 'Pernambuco', 'Capibaribe', 'Celulares', 'Calculadora', 'Impressora', 'Desenvolvimento')
vogais = 0
for c in range(0, len(palavras)):
    novinha = []
    for chr in palavras[c]:
        if chr in "aeiouAEIOU":
            novinha.extend(chr)
            #print(novinha)
    novinha = " ".join(novinha)
    vogais += len(novinha)
    print(f'{palavras[c]} sem as consoantes fica {novinha.lower()}')
print(f'Total de {vogais} vogais')
