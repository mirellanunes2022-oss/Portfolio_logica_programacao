from tarefas import tarefas
import os
os.system('cls')

while True:
    print('\n --- lista de tarefas ---')
    print('1 - adicionar tarefas')
    print('2 - listar tarefas')
    print('3 - sair')
    
    opcao = int(input(' digite a opicao desejada:'))

    if (opcao == 1):
        print('Opção para adicionar uma tarefa!')
    elif (opcao == 2):
        print('Opção para listar tarefas!')
    elif (opcao == 3):
        print('Programa encerrado!')
        break
    else:
        print('Número inválido')