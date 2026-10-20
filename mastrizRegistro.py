import os
os.system('cls')

# Importa a biblioteca os, que permite executar comandos do sistema operacional
import os

# Limpa o terminal/tela.
# No Windows, 'cls' limpa o terminal.
os.system('cls')


# ============================================================
# CRIAÇÃO DA MATRIZ
# ============================================================

# A matriz possui:
# - 3 linhas
# - 4 colunas
#
# Podemos visualizar assim:
#
#          Coluna
#          1  2  3  4
# Linha 1  2  5  1  4
# Linha 2  7  0  3  8
# Linha 3  6  9  2  5

matriz = [[2,5,1,4],
          [7,0,3,8],
          [6,9,2,5]]


# ============================================================
# SOMA DE TODOS OS ELEMENTOS DA MATRIZ
# ============================================================

# Cria uma variável para armazenar o resultado da soma.
# Começamos com 0 porque ainda não somamos nenhum número.
acumulador = 0

# O primeiro for percorre as linhas da matriz.
# range(0,3) gera: 0, 1, 2
#
# Esses números representam os índices das 3 linhas:
# índice 0 -> primeira linha
# índice 1 -> segunda linha
# índice 2 -> terceira linha
for linha in range(0,3):

    # O segundo for percorre as 4 colunas.
    # range(0,4) gera: 0, 1, 2, 3
    for coluna in range(0,4):

        # Acessa o elemento que está na linha e coluna atuais
        # e adiciona esse valor ao acumulador.
        #
        # matriz[linha][coluna]
        #
        # Exemplo:
        # matriz[0][0] -> 2
        # matriz[0][1] -> 5
        # matriz[1][0] -> 7
        acumulador = acumulador + matriz[linha][coluna]


# Exibe a soma de todos os elementos da matriz.
print(f'A soma de toda a matriz resultou em {acumulador}')


# ============================================================
# SOMA DA LINHA 1
# ============================================================

# Zera o acumulador para podermos fazer uma nova soma.
acumulador = 0

# Percorre todas as 4 colunas da primeira linha.
#
# matriz[0][coluna]
#
# O índice 0 representa a primeira linha.
for coluna in range(0,4):

    # Adiciona ao acumulador o elemento da primeira linha.
    acumulador = acumulador + matriz[0][coluna]

# Exibe o resultado da soma da primeira linha.
print(f'A soma da linha 1 é {acumulador}')


# ============================================================
# SOMA DA LINHA 2
# ============================================================

# Zera novamente o acumulador.
acumulador = 0

# Percorre todas as colunas da segunda linha.
#
# O índice 1 representa a segunda linha.
for coluna in range(0,4):

    # Adiciona ao acumulador o elemento da segunda linha.
    acumulador = acumulador + matriz[1][coluna]

# Exibe o resultado da soma da segunda linha.
print(f'A soma da linha 2 é {acumulador}')


# ============================================================
# SOMA DA LINHA 3
# ============================================================

# Zera novamente o acumulador.
acumulador = 0

# Percorre todas as colunas da terceira linha.
#
# O índice 2 representa a terceira linha.
for coluna in range(0,4):

    # Adiciona ao acumulador o elemento da terceira linha.
    acumulador = acumulador + matriz[2][coluna]

# Exibe o resultado da soma da terceira linha.
print(f'A soma da linha 3 é {acumulador}')


# ============================================================
# QUANTIDADE DE LINHAS, COLUNAS E ELEMENTOS
# ============================================================

# len(matriz) retorna a quantidade de linhas da matriz.
#
# Neste caso:
# len(matriz) -> 3
numeroLinhas = len(matriz)


# len(matriz[0]) retorna a quantidade de elementos
# da primeira linha.
#
# Como cada linha possui 4 elementos:
# len(matriz[0]) -> 4
numeroColunas = len(matriz[0])


# Para descobrir a quantidade total de elementos,
# multiplicamos:
#
# número de linhas × número de colunas
#
# 3 × 4 = 12
totalElementos = numeroColunas * numeroLinhas


# Exibe as informações sobre o tamanho da matriz.
print(f'A matriz tem {numeroLinhas} linhas e {numeroColunas} colunas, possuindo {totalElementos} elementos')


# ============================================================
# TRANSFORMAÇÃO DA MATRIZ PARA ROW-MAJOR
# ============================================================

# Cria uma lista vazia.
#
# Essa lista será usada para armazenar os elementos da matriz
# seguindo a ordem ROW-MAJOR.
listaDaMatriz = []


# Percorre todas as linhas da matriz.
for linha in range(numeroLinhas):

    # Para cada linha, percorre todas as suas colunas.
    for coluna in range(numeroColunas):

        # Adiciona o elemento atual da matriz na lista.
        #
        # A ordem será:
        #
        # Primeira linha:
        # 2, 5, 1, 4
        #
        # Segunda linha:
        # 7, 0, 3, 8
        #
        # Terceira linha:
        # 6, 9, 2, 5
        #
        # Resultado:
        # [2, 5, 1, 4, 7, 0, 3, 8, 6, 9, 2, 5]
        listaDaMatriz.append(matriz[linha][coluna])


# Exibe a matriz transformada em uma lista no formato ROW-MAJOR.
print(f'A Matriz em Row-Major fica dessa forma:\n {listaDaMatriz}')


# ============================================================
# DESCOBRINDO A POSIÇÃO DE UM ELEMENTO NO ROW-MAJOR
# ============================================================

# Solicita ao usuário o número da linha.
#
# Aqui o usuário informa a linha começando por 1,
# ou seja:
#
# 1 -> primeira linha
# 2 -> segunda linha
# 3 -> terceira linha
linha = int(input('Em qual linha está o número da matriz que você deseja descobrir a nova posição na lista row-major?'))


# Solicita ao usuário o número da coluna.
#
# Da mesma forma:
#
# 1 -> primeira coluna
# 2 -> segunda coluna
# 3 -> terceira coluna
# 4 -> quarta coluna
coluna = int(input('Em qual coluna está o número da matriz que você deseja descobrir a nova posição na lista row-major?'))


# ============================================================
# CÁLCULO DO OFFSET / POSIÇÃO NO ROW-MAJOR
# ============================================================

# Fórmula do Row-Major:
#
# offset = (linha - 1) * número_de_colunas + (coluna - 1)
#
# O "-1" é necessário porque o usuário informa linha e coluna
# começando em 1, enquanto os índices da lista Python começam
# em 0.
#
# Exemplo:
#
# Se o usuário escolher:
# linha = 2
# coluna = 3
#
# Temos:
#
# offSet = (2 - 1) * 4 + (3 - 1)
# offSet = 1 * 4 + 2
# offSet = 6
#
# O elemento matriz[1][2] é o número 3.
# Na lista Row-Major:
#
# [2, 5, 1, 4, 7, 0, 3, 8, 6, 9, 2, 5]
#                       ↑
#                    índice 6
#
# Portanto, o número 3 está na posição 6.
offSet = (linha - 1) * numeroColunas + (coluna - 1)


# Exibe:
# - o número escolhido na matriz
# - a posição desse número na lista Row-Major
#
# Usamos linha-1 e coluna-1 para acessar corretamente
# o elemento da matriz usando os índices do Python.
print(f'O número {matriz[linha-1][coluna-1]} da matriz está na posição {offSet} da lista ROW-MAJOR')

