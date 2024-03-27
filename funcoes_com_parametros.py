"""
# Funçeõs com Parâmetros:

- Funções com parâmetros recebem dados para serem
processados dentro das mesmas.

- Se a gente pensar em um programa qualquer, geralmente teremos:
ENTRADA => PROCESSAMENTO => SAÍDA

- Se a gente pensar em funões, já sabemos que temos funções que:
* Não possuem entrada;
* Não possuem saída;
* Possuem entrada, mas não possuem saída;
* Não possuem entrada, mas possuem saída;
* Possuem entrada e saída.


# Refatorando a função quadrado_de_sete():
def quadrado(number):  # Number é um parâmetro obrigatório.
	return number ** 2

print(f"quadrado(7) = {quadrado(7)}")
print(f"quadrado(2) = {quadrado(2)}")
print(f"quadrado(5) = {quadrado(5)}")
print(15*'-')

# print(quadrado()) # => TypeError: quadrado() missing 1 required
# positional argument: 'number'

# Refatorando a função cantar_parabéns:
def cantar_parabens(aniversariante):
	print("Parabens pra você")
	print("Nesta data querida")
	print("Muitas felicidades")
	print("Muitos anos de vida")
	print(f"Viva o/a {aniversariante}")

cantar_parabens("Marcos")
print(15*'-')

Observação: Funções podem ter 'n' parâmetros de entrada, ou seja, podemos
receber como entrada em uma função quantos parâmetros forem necessários.
Eles geralmente são separados por vírgulas.


def sum(a, b):
	return a + b

def multiplication (number1, number2):
	return number1 * number2

def other_function(number1, b, msg):
	return (number1 + b)*msg

print(sum(2,5))
print(sum(10,20))
print(multiplication(4,5))
print(multiplication(2,8))
print(other_function(3, 2, 'Geek '))
print(other_function(5, 4, 'Python '))
print(15*'-')

# Observações:
# 1) Se a gente informar um número errado de parâmetros ou argumentos,
# teremos um TypeError.

# print(sum(2, 3, 4)) # => TypeError: sum() takes 2 positional
# arguments but 3 were given => Argumentos a mais.

# print(sum(2)) # => TypeError: TypeError: sum() missing 1 required
# positional argument: 'b' => Argumentos a menos

# Nomeando Parâmetros:

def nome_colpeto(nome, sobrenome): # 'nome' e 'sobrenome' => são parâmetros
	return f"Seu nome completo é : {nome} {sobrenome}."

print(nome_colpeto("Angelina", "Jolie"))
# 'Angelina' e 'Jolie' são argumentos.

print(15*'-')

nome_1 = 'Felicity'
sobrenome_1 = 'Jones'

print(f"nome_colpeto(nome_1, sobrenome_1) = "
	  f"{nome_colpeto(nome_1, sobrenome_1)}")
print(15*'-')
print(f"nome_colpeto(sobrenome_1, nome_1) = "
	  f"{nome_colpeto(sobrenome_1, nome_1)}")
print(15*'-')

# Observações importantes em funções no Python:
# 1) Diferença entre parâmetros e argumentos:
# Parâmetros: São variáveis declaradas na definição de uma função.
# Argumentos: São dados passados durante a esecução de uma função.

# 2) A ordem dos parâmetros importa.

# Argumentos Nomeados - Keyword Arguments:
# Caso utilizemos nomes dos parâmetros como argumentos para informá-los,
# podemos utilizar qualquer ordem.

print(nome_completo(nome="Angelina", sobrenome="Jolie"))
print(15*'-')
print(nome_completo(nome=nome_1, sobrenome=sobrenome_1))
print(15*'-')
print(nome_colpeto(sobrenome="Marques", nome="Marcia"))
print(15*'-')


"""

# Erro comum na utilização do 'return' em Python:

def soma_impares(numeros):
	total = 0
	for num in numeros:
		if num % 2 != 0:
			total = total + num

	return total


list_1 = [1, 2, 3, 4, 5, 6, 7]

print(f"soma_impares(list_1) = {soma_impares(list_1)}")
print(15*'-')

tuple_1 = tuple(list_1)

print(f"soma_impares(tuple_1) = {soma_impares(tuple_1)}")
