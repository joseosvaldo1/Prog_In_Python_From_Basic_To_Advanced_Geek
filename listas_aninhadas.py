"""
# Listas Aninhadas (Nested Lists):

- Algumas linguagens de programação possuem uma estratutura de dados
chamadas de array:
* Arrays unimensionais (também chamados de arrays/vetores);
* Arrays multidimensionais (também chamados de matrizes).

- Em Python, temos as listas.

numbers = [1, 2, 3, 4, 5, 6]
list_1 = [1, 'b', 3.234, True, 5]

listas = [[1,2,3], [4, 5, 6], [7, 8, 9]] # => Seria uma matriz 3x3

print(f"listas = {listas}")
print(15*'-')
print(f"type(listas) = {type(listas)}")
print(15*'-')

# Como fazemos para acessar os dados da list_2:

print(f"listas[0] = {listas[0]}")         # => list_2[0] = [1, 2, 3]
print(f"listas[0][1] = {listas[0][1]}")   # => list_2[0][1] = 2
print(f"listas[2][1] = {listas[2][1]}")   # => list_2[2][1] = 8
print(15*'-')

# Iterando com loops em uma lista aninhada:

for lista in listas:
	print(lista)

print(15*'-')

for lista in listas:
	for valor in lista:
		print(valor)
		print(5*'-')

	print(10*'-')

print(15*'-')

# List Comprehension em Lista Aninhadas:
[[print(valor) for valor in lista] for lista in listas]
print(15*'-')


"""

# Outros Exemplos:

# Gerando um tabuleiro/matriz 3 x 3:

			# Lines								# Columns
board = [[number for number in range(1,4)] for value in range(1,4)]
print(board)
print(15*'-')

# Gerando jogadas para o jogo da velha:

hash_velha = [['X' if number % 2 == 0 else 'O' for number in range(1,4)]
			  for value in range(1,4)]

print(f"hash_velha = {hash_velha}")

print(15*'-')

# Gerando valores iniciais:

print([['*' for i in range(1,4)] for j in range(1,4)])