import os
os.system('cls|| clear') 

nota1 = float(input('digite a primeira nota\n'))
nota2 = float(input('digite a segunda nota\n'))

media = (nota1 + nota2)/2

if (media >= 6):
    print('voce foi aprovado(a)')
else:
    
    print('voce foi reprovado(a)')
