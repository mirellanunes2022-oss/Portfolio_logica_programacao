import os
os.system('cls|| clear') 

print("Digite sua idade")
idade = int(input())

if (idade >= 0) and  (idade<=12) :
  print("Você é uma criança")
if ( idade >= 13) and (idade<=17):
  print("Você e um adolecente")
if(idade >= 18) and (idade <=64):
  print('Você e um adulto')
if (idade > 65):
    print("Você e um idoso")
  
  
  