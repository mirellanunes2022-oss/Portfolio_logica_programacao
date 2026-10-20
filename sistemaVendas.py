import os
os.system('cls|| clear') 

print(' Digite o valor total')
total = float(input())
if (total > 100) and (total < 500):
    print('Você ganhou 5% de desconto:', total * 0.05)
if (total > 500):
    print('Você ganhou 10% de desconto:',total * 0.10)
if (total < 200):
    print('Você possui um frete de 15 reais')
