Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 05/05/2026
Var
// Seção de Declarações das variáveis 
idade: inteiro
mensagem_final: caractere
 
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreval("Digite a idade do cliente:")
leia(idade)
 
se (idade <=12) ou (idade >=60)entao
   mensagem_final <- "o cliente tem direito a desconto"
senao
   mensagem_final <- "o cliente nao tem direito a desconto"
fimse
 
escreval (mensagem_final)
Fimalgoritmo
