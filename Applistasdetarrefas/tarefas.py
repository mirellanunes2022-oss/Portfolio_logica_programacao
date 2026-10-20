import os
os.system('cls')

lista_tarefas= []

def criar_tarefa(nome_tarefa):
    tarefa = {'nome': nome_tarefa, 'concluída': False}
    lista_tarefas.append(tarefa)
    print(f'Tarefa {tarefa} foi adicionada com sucesso')

def listar_tarefa():
    contador = 1
    for tarefa in lista_tarefas:
        if tarefa['concluída'] == True:
            status = 'Concluída'
        else:
            status = 'Pendente'

        print(str(contador) + '.' + tarefa["nome"] + '[' + status + ']')
        contador += 1
    
def atualizar_tarefa(indice_usuario):
    indice_real = indice_usuario - 1
    lista_tarefas[indice_real]['concluída'] = True
    print('Tarefa atualizada como "concluída"')

def apagar_tarefa(indice_usuario):
    indice_real = indice_usuario - 1

    lista_tarefas.pop(indice_real)

import os
import time
from tarefas import lista_tarefas, criar_tarefa, listar_tarefa, atualizar_tarefa, apagar_tarefa
os.system('cls')

def executar_menu():
    while True:
        time.sleep(2)
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
        elif (opcao == 1):
            nome = str(input('Digite o nome da tarefa: '))
            criar_tarefa(nome)
        elif (opcao == 2):
            listar_tarefa()
        elif (opcao == 3):
            numero_tarefa = int(input('Digite o número da tarefa que será atualizada como "concluída"'))
            atualizar_tarefa(numero_tarefa)
        elif (opcao == 4):
            numero_tarefa = int(input('Digite o número da tarefa que será apagada'))
            apagar_tarefa(numero_tarefa)
            
executar_menu()