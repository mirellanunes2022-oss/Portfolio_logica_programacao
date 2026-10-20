import os
os.system('cls|| clear') 

#pontuacao do jogador
pontuacao = [80,100,60,120]

# inicializando as variaveis para coletar estatisticas
soma = 0
maior = pontuacao[0] #80
menor =pontuacao[0]#80

# 1° rodada
#soma = soma + pontuacao[0]
#2° rodada
#soma = soma + pontuacao[1]
#3 rodada
#soma = soma + pontuacao[2]
#4 rodada
#soma = soma + pontuacao[3]

#if (pontuacao[0] > maior):
  #  maior = pontuacao[0]
#if (pontuacao[1] > maior):
 #   maior = pontuacao[1]
#if (pontuacao[2] > maior):
  #  maior = pontuacao[2]
#if (pontuacao[3] > maior):
 # maior = pontuacao[3]
    
#print(f"o maior numero e {maior}")

for i in range(4):
    soma = soma + pontuacao[i]
    
    print(soma)
    
for i in range(i):
    soma = soma + pontuacao[i]
    if ( pontuacao[i] > maior):
        maior = pontuacao[i]
        print(maior)

    