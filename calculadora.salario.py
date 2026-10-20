import os
os.system('cls|| clear') 

SB = float(input('Digite o salario bruto'))
D = float(input('Digite quantos dependentes voce tem'))
Pr = float(input('Digite o valor da previdencia'))
Ps = float(input('Digite o valor da pensão'))

if SB <0 or D <0 or Pr <0 or Ps <0:
    print('Erro de validação')
    base = salario - (dependentes * 189.59)- previdencia - pensao
    if base <0:
        imposto = 0
    elif base <= 2826.65:
        
