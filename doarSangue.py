import os
os.system('cls|| clear')

 idade= int(input('digite sua idade: '))
peso = float(input('digite seu peso: '))

if (idade >= 18) and (idade <= 69) and (peso > 50):
    print(' voce esta elegivel para doar sangue')
else:
    print(' voce esta inlegivel par doar sangue')
    