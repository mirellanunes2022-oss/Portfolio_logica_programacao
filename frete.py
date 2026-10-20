import os
os.system('cls|| clear') 

peso = float(input('digite o peso do pacote:'))
if(peso> 10):
    print('frete expresso')
elif(peso>2):
    print("frete economico")
else:
    tipofrete = str(input(" digite o tipo de frete:"))