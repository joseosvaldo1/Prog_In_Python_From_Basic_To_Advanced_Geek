"""
# Definindo Funções:

- Funções são pequenas partes de código que realizam tarefas específicas,
- Funçeõs podem ou não receber entradas de dados e retornar uma saída de
dados;
- Elas são muito úteis para executar procedimentos similares por repetidas
vezes.

# Observação: Se você escrever uma função que realiza várias tarefas dentro
dela, é bom fazer uma verificação para que a função seja simplificada.


- Já utilizamos várias funções desde o início do curso: print(), min(),
max(), count(), len() etc.


# Exemplo de utilização de funções em Python:

colors = ['green', 'yellow', 'blue', 'white']

# Utilizando uma função integrada (built-in) do Python - print():

print(colors) # => Output: ['green', 'yellow', 'blue', 'white']

course = "Programação em Python: Essencial"
print(course) # => Output: Programação em Python: Essencial

colors.append('purple')
print(colors) # => Output: ['green', 'yellow', 'blue', 'white', 'purple']

# course.append("Mais Dados ...") # => AttributeError: 'str' object has
# no attribute 'append'

colors.pop()

print(colors) # => Output: ['green', 'yellow', 'blue', 'white']

# Funções favorecem a boa prática de DRY - Dont Repeat Yoursel - Não
# Repita Você Mesmo ( ou Não se repita / Não Repita seu Código).

# Em Python, a forma geral de se definir uma função é:
# def nome_da_função(parâmetros_de_entrada):
#     <bloco_da_função>
#

# Onde:
# nome_da_função: sempre com letras minúsculas e, se for composto,
# separado por underlines (snake case)
# parâmetros_de_entrada: Opicionais, onde havendo mais de um parâmetro
# ocorrerá a separação por vírgulas, podendo ser opicionais ou não.
# bloco_da_função: Também chamado de corpo_da_função ou implementação da
# função, é onde o processamento da função ocorre. Neste bloco, pode ou
# não ocorrer o retorno da função

# Observação: Observe que, para definir uma função, utilizamos a palavra
# reservada 'def' informando ao Python que estamos definindo uma função
# Também abrimos o bloco de código com o dois pontos (:) o qual é usado
# em Python para definir blocos de códigos.



"""

# Exemplo_1:

# Definindo a primeira função:

# Definição da função 'say_hi()':
def say_hi():
	print("Hi!")

# Observações:
# 1) Veja que, dentro de nossas funções, podemos utilizar outras funções;
# 2) Veja que nossa função só executa uma única tarefa, a única coisa
# que ela faz é dizer "Hi";
# 3) Veja que está função não recebe nenhum parâmetro de entrada.
# 4) Veja que esta função não retorna nada.


# Utilizando a função 'say_hi()':
# Chamada de Execução:
say_hi()

# ATENÇÃO: Nunca esqueça de usar os parênteses ao executar uma função;
# say_hi   =>  Errado
# say_hi () => Errado
# say_hi() =>  Correto

print(15*'-')

# Exemplo_2:
def cantar_parabens():
	print("Parabens pra você")
	print("Nesta data querida")
	print("Muitas felicidades")
	print("Muitos anos de vida")
	print("Viva o aniversariante")

cantar_parabens()

print(15*'-')

# for n in range(5):
# 	print(n)
# 	print(10 * '_')
# 	cantar_parabens()
# 	print(10*'_')

# Em Python, podemos inclusive criar variáveis do tipo de uma função
# e executar essa função através da variavél.

canta = cantar_parabens
canta()