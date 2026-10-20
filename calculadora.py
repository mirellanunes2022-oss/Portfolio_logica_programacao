import os
os.system('cls|| clear') 

SB = float(input('Digite o salario bruto \n'))
D = float(input('Digite quantos dependentes voce tem \n'))
Pr = float(input('Digite o valor da previdencia \n'))
Ps = float(input('Digite o valor da pensão \n'))

if (sb <= 2112):
  print('Sua alíquota é 0')
  a = sb * 0 
elif (sb >= 2112.01) and (sb <= 2826.65):
# elif (sb <= 2826.65):
  print('Sua alíquota é de 7,5%')
  a = Sb * 0.075
elif (sb >= 2826.66) and (sb <= 3751.05 ):
  a = sb * 0.15
  print('Sua alíquota é de 15%')
elif (sb >= 3751.06) and (sb <= 4664.68):
  print('Sua alíquota é de 22,5%')
  a = sb * 0.225
else:
  print('Sua alíquota é de 27,5%')
  a = sb * 0.275

total = a + (dp * 189.59) + pr + ps
sl = sb - total

print('Você ganha: R$', sb, 'de salário bruto')
print('Seus descontos são de R$', total)
print('O seu salário líquido é de R$', sl)