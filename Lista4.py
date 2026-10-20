import os
os.system('cls|| clear') 

carros = ["gol quadrado", "astra", "vectra", "nivus"]

carros += ["creta"]#['gol quadrado']

carros.append("civic")
#append adiciona item no final da lista

carros.insert(0, "fusca")
#insert adiciona um item a uma determinada posição
print(carros)

carros.remove("astra")
#remove deleta um item pelo seu valor
print(carros)

carros.pop(2)
#pop remove um itemm pelo seu index (posicao)
print(carros) #['funca','gol quadeado', 'nivus', 'creta'', civic']
numeros = [5,6,7,9,4,3,10,20,-3]
print(numeros)

numeros.sort()
# sort organiza em ordem crescente uma lista de números
print(numeros)

numeros.reverse()
# reverse inverte a ordem da lista
print(numeros)