import os
os.system('cls|| clear') 

print('Digite o primeira nota')
nota1 = float(input())
print('Digite o segunda nota')
nota2 = float(input())
print('Digite o terceira nota')
nota3 = float(input())
print('Digite a frequencia')
frequencia = float(input())

media = (nota1+nota2+nota3)/3

if (frequencia < 75):
  print('Você foi reprovado direto')
else:
 if (media >= 7):
     print('Você foi aprovado(a) por frequência e média. Sua média foi:', media)
 elif (media >= 4) and (media <= 6.9):
   print('Você foi aprovado (a) por frequência, mas ficou de recuperação por média.')
   ('Sua média foi:', media)
 else:
   print('Você foi reprovado por média. Sua média foi:', media)
   