"""
# Funções de Maior Grandeza:
- Em inglês, Higher Order Functions - HOF:

- O que isso significa?
- Quando uma linguagem de programação suporta HOF, indica que
podemos ter funções que retornam outras funções ou mesmo que
podemos passar funções como argumentos de outras funções e,
até mesmo, criar variáveis do tipo de funções em nossos
programas.

Observação: Na seção de funções, utilizamos o conceito de HOF.

- Em Python, as funções são "cidadãos de primeira classe". Em
inglês são "First Citizen Class".


# ---------------------------------------------------------------

# Exemplos - Definindo as funções:

def add(a, b):
	return a + b


def decrease(a, b):
	return a - b


def multiply(a, b):
	return a * b


def divide(a, b):
	return a / b


def calculate(number_1, number_2, function):
	return function(number_1, number_2)


# Testando as funções:
print(f"calculate(4,3,add) = "
	  f"{calculate(4,3, add)}")
print(f"calculate(4,3,decrease) = "
	   f"{calculate(4,3, decrease)}")
print(f"calculate(4,3,multiply) = "
	  f"{calculate(4,3, multiply)}")
print(f"calculate(4,3,divide) = "
	  f"{calculate(4,3, divide):.2f}")

print(30*'-')


# ---------------------------------------------------------------

# Nested Functions - Funções Aninhadas:

# Em Python, podemos também ter funções dentro de funções as
# quais também são conhecidas por Nested Functions ou Inner
# Functions (Funções Internas).

# Exemplos:

from random import choice

def greeting(person):
	def humor():
		return choice(['E aí, ', 'Suma daqui, ', 'Gosto muito de você, '])
	return humor() + person + "!"  # => Retornando a execução da
								   # 	função humor()


# Testando:

print(greeting("Marcos"))
print(15*'-')
print(greeting("Felicity"))
print(15*'-')


# ---------------------------------------------------------------

# Retornando funções de outras funções:

from random import choice

def makes_me_laugh():
	def laugh():
		return choice(['hahahahaha', 'kkkkkkkk', 'yayayayaya'])
	return laugh  # => Retornando a função laugh e nao a execução dela.

# Testando:
rindo = faz_me_rir()
print(rindo())


# ---------------------------------------------------------------

"""


from random import choice

# Inner Functions(Funções Internas) / Nested Functions podem
# acessar o escopo de funções mais externas.

def makes_me_laugh_again(person):
	def laughing():
		laughter = choice(('hahahaha', 'lolololol', 'kkkkkkkk'))
		return f"{laughter} {person}"
	return laughing


# Testando:

laughing = makes_me_laugh_again('Fernanda')
print(laughing())
print(laughing())
print(laughing())

