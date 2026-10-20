import os
os.system('cls|| clear')

loja = ['prateleira1', 'prateleira2', 'prateleira3', 'prateleira4', 'prateleira5']

prateleiras = ['produto1','produto2','produto3','produto4','produto5','produto6','produto7','produto8','produto9','produto10']

print(loja[0], prateleiras[0])
print(loja[0], prateleiras[1])
print(loja[0], prateleiras[2])

loja = ['prateleira1', 'prateleira2', 'prateleira3', 'prateleira4', 'prateleira5']

prateleiras = ['produto1','produto2','produto3','produto4','produto5','produto6','produto7','produto8','produto9','produto10']

for prateleira in range(5):
    for produtos in range(10):
        print(loja[prateleira], prateleiras[produtos])