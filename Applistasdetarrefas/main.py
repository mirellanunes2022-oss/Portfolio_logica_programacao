import os
from tarefas import lista_tarefas
os.system('cls')

def executar_menu():
    while True:
        print('\n---------Menu Principal---------')
        print('1. Criar Tarefa')
        print('2. Listar Tarefa(s)')
        print('3. Atualizar Tarefa')
        print('4. Apagar Tarefa')
        print('5. Sair')

        opcao = int(input('Escolha uma opção: '))
        if (opcao == 5):
         print('Programa Encerrado. Tchau!')
        break

executar_menu()

        