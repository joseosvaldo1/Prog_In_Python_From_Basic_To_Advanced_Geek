"""
# Doctests:

- Doctests são testes que colocamos na DocStrings das funções/
métodos do Python.
- Para rodar um teste do doctest, devemos utilizar o seguinte
comando: python -m doctest -v nome_do_modulo.py

# ---------------------------------------------------------


# Exemplo_1:

def sum(a, b):
	'''
	This function sums the numbers a and b.

	# >>> sum(1, 2)
	3

	# >>> sum(4, 6)
	10
	'''
	return a + b


# Saída do doctest:

# python -m doctest -v doctests.py
# Trying:
#     sum(1, 2)
# Expecting:
#     3
# ok
# Trying:
#     sum(4, 6)
# Expecting:
#     10
# ok
# 1 items had no tests:
#     doctests
# 1 items passed all tests:
#    2 tests in doctests.sum
# 2 tests in 2 items.
# 2 passed and 0 failed.
# Test passed.


# print(sum(3, 4))  # => 7


# ---------------------------------------------------------


# Outro exemplo - aplicando TDD:

def duplicate_values(values):
	'''
	Duplicate values in a list.

	# >>> duplicate_values([1, 2, 3, 4])
	[2, 4, 6, 8]

	# >>> duplicate_values([])
	[]

	# >>> duplicate_values(['a', 'b', 'c'])
	['aa', 'bb', 'cc']

	# >>> duplicate_values([True, None])
	Traceback (most recent call last):
		...
	TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
	'''

	return [2*item for item in values]


# ---------------------------------------------------------

# Erro inesperado:


def say_hi():
	'''
	This function say 'Hi'.

	# >>> say_hi()
	'Hi'

	'''

	return "Hi"

# Observação: Dentro do Doctest, o interpretador do Python não
# reconhece strings com aspas duplas. Devemos utilizar as
# aspas simples obrigatoriamente.


# ---------------------------------------------------------

"""


# Um último caso estranho:

def verity():
	'''
	This function returns True.

	:return: True

	>>> verity()
	True
	'''
	return True



