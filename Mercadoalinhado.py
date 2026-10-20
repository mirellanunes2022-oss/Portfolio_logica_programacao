import os
os.system('cls|| clear') 
prateleiras = ['prateleira1', 'prateleira2','prateleira3', 'prateleira4', 'prateleira5',]

produtos = ['produto1','produto2','produto3','prateleira4',]

print(prateleira(0), produtos(0))
print(prateleira(0), produtos(1))
print(prateleira(0), produtos(2))
print(prateleira(0), produtos(3))
print(prateleira(1), produtos(0))

for i in range(5):
    for j in range(4):
      print( prateleiras(i), produtos (j))
    
for pratileira in prateleiras:
    for produto in produtos:
        print(pratileira,produto) 
        
    print(f"prateleira, produto")
    
    

