import  os
os.system('cls|| clear') 

n = int(input("Digite a quantidade de valores N: "))

lista = {}
for i in range(n):
    valor = float(input(f"Digite o {i+1} valor: "))
    lista.append(valor)

print("\n Valores anotados:")
for i, valor in enumerate(lista):
    print(f"Valor {i+1}: {valor}")
    
