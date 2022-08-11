a = float(input('Sua altura em metros (Ex: 1.76): '))
p = float(input('Seu peso em quilos (Ex: 90): '))
imc = p / (a * a)
print('Seu \033[1:34mIMC\033[m é {:.1f}'.format(imc))
if imc < 18.5:
    print('Baixo peso. REF: Até 18.5kg \033[1:34mBaixo\033[m')
elif imc >= 18.5 and imc < 25:
    print('Peso normal. REF: Entre 18.5 e 24.9 \033[1:34mMédio\033[m')
elif imc >= 25 and imc < 30:
    print('Pre-Obeso. REF: Entre 25 e 29.9 \033[1:34mAumentado\033[m')
elif imc >= 30 and imc < 35:
    print('Obesidade I. REF: Entre 30 e 34.9 \033[1:34mModerado\033[m')
elif imc >= 35 and imc < 40:
    print('Obesidade II. REF: Entre 35 e 39.9 \033[1:34mGrave\033[m')
else:
    print('Obesidade III. REF: Acima de 40 \033[1:34mMuito Grave\033[m')