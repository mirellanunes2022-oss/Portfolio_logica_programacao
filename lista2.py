import os
os.system('cls')

# Lista – despensa flexível (pode ser modificada) 
frutas_lista = ["maçã", "banana", "laranja"] 
 
# Tupla – despensa fixa (não pode ser modificada) 
temperos_tupla = ("sal", "pimenta", "açúcar") 

# String – despensa de caracteres 
palavra_string = "PYTHON" 

for frutas in frutas_lista:
    print(frutas)

for frutas in temperos_tupla:
    print(frutas)

for letras in palavra_string:
    print(letras)