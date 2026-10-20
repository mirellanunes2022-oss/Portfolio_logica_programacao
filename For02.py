import os
os.system('cls|| clear') 

acumulador = contador = 0

acumulador = 0
contador = 0

for i in range(3):
    print('Bem vindo')
    item = float(input('Digite o valor do item '))
    contador = contador + 1
    acumulador += item
    #acumulador = acumulador + item
    #contador += 1

print(f'Rodou {contador} vezes')
print(f'O preço final foi de R${acumulador}')

# for numero in range(1, 11):
#     print(numero)

# for numero in range(1,101,2):
#     print(numero)

# for numero in range(10,-1,-1):
#     print(numero)

# for contador in range(1,11):
#     print(f'5 x {contador} = {5*contador}')
#     #print('5 x', contador,'=',5*contador)

for n in range(1,100,2):
    print(n)

for n in range (0,100):
    if (n%2>0):
        print(n)