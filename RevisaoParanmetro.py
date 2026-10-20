import os

# Importa a biblioteca 'os', que permite interagir com o sistema operacional.
import os

# Limpa a tela do terminal.
# No Windows, 'cls' é o comando usado para limpar a tela.
os.system('cls')


# Esta é uma função chamada 'bemVindo'.
# Ela não recebe nenhum valor como entrada.
# def bemVindo():
#     print('Seja bem-vindo!')

# Aqui estamos chamando/executando a função.
# bemVindo()


# Criamos uma nova função chamada 'bemVindo2'.
# Ela recebe uma informação chamada 'nome'.
def bemVindo2(nome):

    # Mostra uma mensagem na tela utilizando o nome recebido pela função.
    # O 'f' antes das aspas permite colocar uma variável dentro do texto.
    print(f'Seja bem-vindo, {nome}')


# Chamamos a função e passamos 'Guilherme' como argumento.
# Dentro da função, o parâmetro 'nome' recebe o valor 'Guilherme'.
bemVindo2('Guilherme')