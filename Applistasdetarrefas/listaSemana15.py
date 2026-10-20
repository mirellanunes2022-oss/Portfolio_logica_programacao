import os
os.system('cls')

notas=[7,8.5,6,9,5.5]#lista de notas

quantidadeValores= len(notas)#varaiavel recebe a Quantidade de valores através da função len()
indicePrimeiroValor = notas.index(7)#variável recebe o primeiro valor do primeriro indice atráves da função index
ultimoIndice= len(notas)-1#variável recebe o último valor atráves da subtração de 1 sobre número de itens

i =0 #inicializando o índice i com valor 0
while i < len(notas):#estrutura while com condição de parada
    print(notas [i])#mostrar cada item da lista, rodada por rodada
    i +=1#incrementa 1 ao valor do index a cada rodada do while

#contar quantas notas existem
print(len(notas))

#identificar a maior nota:
maior=notas[0]
for i in range(5):
    if(notas[i]>maior):
        maior= notas[i]
print(f'O maior número é {maior}')

#somar todas as notas
soma=0
for i in notas:
    soma+=i
print(soma)