import os
os.system('cls') 

lista = [10,20,30,20,50]

for i in range(len(lista)):
    for j in range(i + 1, len(lista)):
        if lista[i] == lista[j]:
            print("Duplicado encontrado:", lista[i])

