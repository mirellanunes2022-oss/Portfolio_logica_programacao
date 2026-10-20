import os
os.system('cls|| clear') 

import random 
numero_secreto = random.randint(1, 10)
palpite = int(input("adivinhe o numero de 1 a 10: "))
if palpite == numero_secreto:
  print('você acertou!')
else:
  print(" você errou! o numero era", numero_secreto)