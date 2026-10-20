import os
os.system('cls|| clear') 

número = 1
contador = 1
acumulador = 1

while (número != 0):
    número = float(input('Digite a número: '))
    contador = contador * 0
    #contador = 0
    acumulador = acumulador * número

número = 1
acumulador = 1
soma = acumulador * contador
print(f'Você digitou {número} número\nA soma é {soma}')

 