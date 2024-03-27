"""
# Reversed:

- Não confunda a função 'reversed()' com a função 'reverse()'
estudada em listas.

- A função 'reverse()' só funciona em listas.
- A função 'reversed()' funciona em qualquer iterável.
- A utilidade da função 'reversed()' é inverter a ordem dos
elementos do iterável
- A função 'reversed()' retorna um iterável chamado 'list_reverse
iterator'.

"""


# Exemplos:

lista = [1, 2, 3, 4, 5]
result_list = reversed(lista)
result_tuple = reversed(lista)
result_set = reversed(lista)

print(f"lista original: {lista}")
print(f"result: {result_list}")
print(f"type(result): {type(result_list)}")
print(15*'-')
# Podemos converter o list_reverse iterator retornado em
# uma lista, uma tupla ou um set:

# Lista:
print(f"lista invertida= {list(result_list)}")


# Tuple:
print(f"tupla invertida= {tuple(result_tuple)}")

# Set:
print(f"set invertido= {set(result_set)}")

print(15*'-')
# Observação: Em conjuntos (set), não definimos a ordem
# dos elementos.

# Podemos iterar sobre o 'list_revese itarator':

for letter in reversed('Geek University'):
	print(letter, end='')

print("\n")
print(15*'-')

# Podemos fazer a mesma iteração anterior sem o uso do for:

print(f"''.join(list(reversed('Geek University'))) = "
	  f"{''.join(list(reversed('Geek University')))}")

print(15*'-')

# Podemos obter o mesmo resultado acima usando slice:
print(f"'Geek University'[::-1] = {'Geek University'[::-1]}")

print(15*'-')

# Podemos também utilizar a função 'reversed()' para
# fazer um loop 'for' reverso:

for number in reversed(range(0, 10)):
	print(number)

print(15*'-')

# Podemos obter o mesmo resultado acima usando apenas o range:

for number in range(9, -1, -1):
	print(number)

print(15*'-')