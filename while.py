import os
os.system('cls')

nota = 0
contador = 0
acumulador = 0

while (nota != -1):
    nota = float(input('Digite a nota: '))
    contador = contador + 1
    #contador += 1
    acumulador = acumulador + nota

contador -= 1
acumulador += 1
media = acumulador / contador
print(f'Você digitou {contador} notas\nA média é {media}')