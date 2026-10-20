import os
os.system('cls|| clear') 

acumulador = 0
for contador in range(1,4):
    item = float(input(f'Digite o valor do item {contador}: '))
    acumulador += item

print(acumulador)


