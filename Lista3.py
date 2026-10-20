import os 
os.system("cls")

#Uma lista é uma estrutura usada para guardar vários valores em uma única variável.
nomes = ["Ana", "Carlos", "João"]
idades = [15, 16, 17]
notas = [8.5, 7.0, 9.2]

# Cada item da lista possui uma posição, chamada de índice. Começa em 0
print(nomes[2])
print(idades[1])
print(notas[0])



#Podemos alterar uma lista chamando a posição dela e atribuindo um novo valor
frutas = ['melão', 'abacaxi', 'pêra']
print(f'Frutas iniciais: {frutas}')
frutas[0] = "laranja"
print(f'Frutas pós modificação: {frutas}')