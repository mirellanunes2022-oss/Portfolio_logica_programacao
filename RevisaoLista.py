import os
os.system('cls|| clear') 

Cores = ['Azul,' 'Amarelo,' 'Branco,' 'Cinza,' 'Preto']

print(Cores) #mostra a lista por completo
print(Cores[0]) #mostra apenas o 1º item

for cor in Cores:
    print(cor) #mostra todos os elementos de dentro 
    
modificavel = [1,2,3,4,5]
print(modificavel) # [1,2,3,4,5]
modificavel[0] = 0 #1º posicao vira 0
print(modificavel) # [0,2,3,4,5,]

tupla = (1, 2, 3, 4, 5) 
print(tupla) # (1, 2, 3, 4, 5) 
# tupla[0] = 0 
print(tupla) # erro, pois não pode ser alterado

string = 'PYTHON'
print(string[0]) #P