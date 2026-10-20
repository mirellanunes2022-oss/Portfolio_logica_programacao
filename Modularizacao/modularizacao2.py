# Importa o módulo "os".
# Ele permite executar alguns comandos do sistema operacional.
import os

# Limpa a tela do terminal.
# No Windows, "cls" limpa o console.
os.system('cls')


# Criamos uma função chamada "maioridade".
# Uma função é um bloco de código que podemos executar quando quisermos.
def maioridade():

    # Pede o nome da pessoa.
    # O input() sempre recebe o que foi digitado como texto (string).
    nome = input("Nome: ")

    # Pede a idade da pessoa.
    # Como queremos trabalhar com números, usamos int()
    # para transformar o texto digitado em um número inteiro.
    idade = int(input("Idade: "))

    # Verifica se a idade é maior ou igual a 18.
    # Se a condição for verdadeira, executa o código abaixo.
    if idade >= 18:

        # Mostra que a pessoa é maior de idade.
        print(nome, "é maior de idade")

    # Caso a condição do if seja falsa, executamos o else.
    else:

        # Mostra que a pessoa é menor de idade.
        print(nome, "é menor de idade")


# Criamos outra função, chamada "mediaDasNotas".
# Essa função será responsável por calcular a média de duas notas.
def mediaDasNotas():

    # Pede a primeira nota.
    # Usamos float() porque uma nota pode ter casas decimais,
    # por exemplo: 7.5
    nota1 = float(input("Nota 1: "))

    # Pede a segunda nota.
    nota2 = float(input("Nota 2: "))

    # Calcula a média das duas notas.
    # Primeiro somamos as duas notas e depois dividimos por 2.
    media = (nota1 + nota2) / 2

    # Verifica se a média é maior ou igual a 6.
    if media >= 6:

        # Se for verdadeira, mostra "Aprovado".
        print("Aprovado")

    # Se a média for menor que 6, entra no else.
    else:

        # Mostra "Reprovado".
        print("Reprovado")


# Aqui chamamos (executamos) a função mediaDasNotas().
# Quando o Python chega nessa linha, ele entra na função
# e executa todo o código que está dentro dela.
mediaDasNotas()

# Depois que mediaDasNotas() termina,
# o Python continua para a próxima linha.
#
# Aqui chamamos a função maioridade().
# Ela então pede o nome e a idade e verifica se a pessoa
# é maior ou menor de idade.
maioridade()
keep
Fixada