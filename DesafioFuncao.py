import os 
os.system('cls')

def nome(nome):
    print(f'bem vindo, {nome}')
#nome(input('digite seu nome:\n'))

def nomepedir(nome):
    return f'seu nome é {nome}'
ps = nomepedir('Bianca')
#print(ps)

clientes = []

def adicionar(nome):
    clientes.append(nome)

def mostrar():
    print(clientes)

def remover(nome):
    clientes.remove(nome)

def atualizar(n, nome):
    clientes[n] = nome 
  


def nome(nome):
    print(f'bem vindo, {nome}')
#nome(input('digite seu nome:\n'))

def nomepedir(nome):
    return f'seu nome é {nome}'
ps = nomepedir('Bianca')
#print(ps)

clientes = []

def adicionar(nome):
    clientes.append(nome)

def mostrar():
    print(clientes)

def remover(nome):
    clientes.remove(nome)

def atualizar(n, nome):
    clientes[n] = nome
    clientes = []

def adicionar(nome):
    clientes.append(nome)

def mostrar():
    print(clientes)

def remover(nome):
    clientes.remove(nome)

def atualizar(n, nome):
    clientes[n] = nome

def menu():
    resposta = 0

    while resposta != 5:
        resposta = int(input('\nEscolha uma das opções abaixo:\n1. Cadastrar um nome\n2. Mostrar os nomes\n3. Remover um nome\n4. Atualizar um nome\n5. Sair\n'))
        if resposta == 1:
            nome = str(input('Digite o nome que você quer adicionar: '))
            adicionar(nome)
            print('Adicionado com Sucesso!')
        if resposta == 2:
            mostrar()
        if resposta == 3:
            nome = str(input('Digite o nome que você quer remover: '))
            remover(nome)
            print('Removido com Sucesso!')
        if resposta == 4:
            n = int(input('Digite em qual posição está o nome que você quer atualizar: '))
            nome = str(input('Digite o novo nome que você deseja colocar no lugar: '))
            atualizar(n,nome)
            print('Atualizado com Sucesso!')

menu()