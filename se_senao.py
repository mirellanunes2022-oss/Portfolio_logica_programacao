import os
os.system('cls|| clear')

#// Aplicando desconto progressivo
#SE total > 1000 ENTÃO
#desconto ← total * 0.15 // 15% acima de 1000
#SENÃO SE total > 500 ENTÃO
#desconto ← total * 0.10 // 10% acima de 500
#SENÃO
#desconto ← 0 // Sem desconto
# FIM SE

total = 1000

if total > 1000:
  desconto = total * 0.15
elif total > 500:
  desconto = total * 0.10
else:
  desconto = 0
    
print(' seu desconto foi de', desconto, 'reais')
    

