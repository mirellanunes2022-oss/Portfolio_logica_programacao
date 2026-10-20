
# JOGO DA VELHA
# Versão simples para iniciantes


# Criando o tabuleiro 3x3
# O ponto "." representa uma posição vazia


tabuleiro = [
    [".", ".", "."],
    [".", ".", "."],
    [".", ".", "."]
]


# Jogador que começa
jogador = "X"


# Quantidade de jogadas
jogadas = 0


# O jogo continua enquanto não houver vencedor
while True:


    # Mostra o tabuleiro
    print()
    print(tabuleiro[0][0], "|", tabuleiro[0][1], "|", tabuleiro[0][2])
    print("--+---+--")
    print(tabuleiro[1][0], "|", tabuleiro[1][1], "|", tabuleiro[1][2])
    print("--+---+--")
    print(tabuleiro[2][0], "|", tabuleiro[2][1], "|", tabuleiro[2][2])
    print()


    # Pede a posição ao jogador
    posicao = int(input("Jogador " + jogador + ", escolha uma posição (1 a 9): "))


    # Verifica se a posição está entre 1 e 9
    if posicao < 1 or posicao > 9:
        print("Posição inválida!")
        continue


    # Transformando a posição 1-9 em linha e coluna
    if posicao == 1:
        linha = 0
        coluna = 0
    elif posicao == 2:
        linha = 0
        coluna = 1
    elif posicao == 3:
        linha = 0
        coluna = 2
    elif posicao == 4:
        linha = 1
        coluna = 0
    elif posicao == 5:
        linha = 1
        coluna = 1
    elif posicao == 6:
        linha = 1
        coluna = 2
    elif posicao == 7:
        linha = 2
        coluna = 0
    elif posicao == 8:
        linha = 2
        coluna = 1
    elif posicao == 9:
        linha = 2
        coluna = 2


    # Verifica se a posição está vazia
    if tabuleiro[linha][coluna] != ".":
        print("Essa posição já está ocupada!")
        continue


    # Coloca X ou O no tabuleiro
    tabuleiro[linha][coluna] = jogador


    # Conta mais uma jogada
    jogadas = jogadas + 1


    # --------------------------------
    # VERIFICANDO AS LINHAS
    # --------------------------------


    venceu = False


    # Linha 1
    if (tabuleiro[0][0] == jogador and
        tabuleiro[0][1] == jogador and
        tabuleiro[0][2] == jogador):
        venceu = True


    # Linha 2
    elif (tabuleiro[1][0] == jogador and
          tabuleiro[1][1] == jogador and
          tabuleiro[1][2] == jogador):
        venceu = True


    # Linha 3
    elif (tabuleiro[2][0] == jogador and
          tabuleiro[2][1] == jogador and
          tabuleiro[2][2] == jogador):
        venceu = True


    # --------------------------------
    # VERIFICANDO AS COLUNAS
    # --------------------------------


    elif (tabuleiro[0][0] == jogador and
          tabuleiro[1][0] == jogador and
          tabuleiro[2][0] == jogador):
        venceu = True


    elif (tabuleiro[0][1] == jogador and
          tabuleiro[1][1] == jogador and
          tabuleiro[2][1] == jogador):
        venceu = True


    elif (tabuleiro[0][2] == jogador and
          tabuleiro[1][2] == jogador and
          tabuleiro[2][2] == jogador):
        venceu = True


    # --------------------------------
    # VERIFICANDO AS DIAGONAIS
    # --------------------------------


    elif (tabuleiro[0][0] == jogador and
          tabuleiro[1][1] == jogador and
          tabuleiro[2][2] == jogador):
        venceu = True


    elif (tabuleiro[0][2] == jogador and
          tabuleiro[1][1] == jogador and
          tabuleiro[2][0] == jogador):
        venceu = True


    # --------------------------------
    # VERIFICANDO O RESULTADO
    # --------------------------------


    if venceu:
        print()
        print(tabuleiro[0][0], "|", tabuleiro[0][1], "|", tabuleiro[0][2])
        print("--+---+--")
        print(tabuleiro[1][0], "|", tabuleiro[1][1], "|", tabuleiro[1][2])
        print("--+---+--")
        print(tabuleiro[2][0], "|", tabuleiro[2][1], "|", tabuleiro[2][2])
        print()


        print("Jogador", jogador, "venceu!")
        break


    # Se fizer 9 jogadas sem vencedor, é empate
    if jogadas == 9:
        print("Empate!")
        break


    # Troca o jogador
    if jogador == "X":
        jogador = "O"
    else:
        jogador = "X"
