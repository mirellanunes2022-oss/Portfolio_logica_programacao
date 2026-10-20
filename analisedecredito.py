import os
os.system('cls|| clear')

score = int(input('Digite o valor do seu score\n'))
rendaMensal = float(input('Digite o valor da sua renda mensal\n'))


if (score > 600) and (rendaMensal >= 2500):
    print('Empréstimo aprovado')
else:
    emprestimo = float(input('Digite o valor do seu empréstimo\n'))
    fiador = str(input('Você possui um fiador?'))
    if (fiador == 's'):
        scoreFiador = int(input('Digite o score do seu fiador'))
        if (scoreFiador > 700) and (rendaMensal > emprestimo):
            print('Empréstimo aprovado')
        else:
            print('Empréstimo negado')
    else:
        print('Empréstimo negado')
        
