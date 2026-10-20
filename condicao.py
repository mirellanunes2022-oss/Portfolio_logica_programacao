import os
os.system('cls||clear')


bolsa100 = False
nota = 8.5
renda = 1640

print(' o aluno é elegivel para bolsa de 100%', bolsa100)
if (nota <=9) and (renda<=2000):
    print('Você gsnhou ums bolsa de 100%')
    
atleta = True
nota = 8.0
renda = 3000
bolsa50 = (nota >=8 and renda <=3000) or atleta
print(' o aluno é elegivel para bolsa de 50%', bolsa50)
if (nota <=8) and (renda<=3000):
    print('Você ganhou ums bolsa de 50%')