"""
# Decoradores com diferentes assinaturas:
- Funções decoradoras com diferentes parâmetros de entrada.
- Para resolver o problema da quantidade de parâmetros
utilizamos na função decoradora um padrão de projeto chamado
Decorator Pattern o qual corresponde ao uso dos parâmetros
*args e **kwargs.
- A assinatura de uma função é representada pelo seu retorno,
nome e parâmetros de entradas.


# ---------------------------------------------------------

# Relembrando decorators:


def shout_out(function):
	def increase(name):
		return function(name).upper()
	return increase


@shout_out
def greeting(name):
	return f"Hello, I am {name}!"


@shout_out
def ordering(main, accompaniment):
	return (f"I would like to order {main} accompanied "
			f"by {accompaniment} please.")


# Testando:
# print(greeting("Angelina"))

print(ordering("rump steak", "french fires"))
# Saída-output: TypeError: shout_out.<locals>.increase()
# takes 1 positional argument but 2 were given

# Observação: Para resolver o problema acima, utilizamos
# um padrão de projeto chamado Decorator Pattern.

# ---------------------------------------------------------

# Refatorando com o Decorator Pattern:

def shout_out(function):
	def increase(*args, **kwargs):
		return function(*args, **kwargs).upper()
	return increase

@shout_out
def greeting(name):
	return f"Hello, I am {name}!"


@shout_out
def ordering(main, accompaniment):
	return (f"I would like to order {main} accompanied "
			f"by {accompaniment} please.")


# Testando:
print(greeting("Felicity"))

print(15*'-')
print(ordering("rump steak", "french fires"))

print(15*'-')


@shout_out
def lol():
	return 'lol'


print(lol())

print(15*'-')

# Observação: Vale lembrar que podemos utilizar parâmetros
# nomeados

print(ordering(accompaniment="french fires", main="rump steak"))

print(15*'-')

# ---------------------------------------------------------



# ---------------------------------------------------------




"""


# Decorators com argumentos:

def check_first_argument(value):
	def internal(function):
		def other(*args, **kwargs):
			if args and args[0] != value:
				return f"Incorrect value! First value must be {value}!"
			return function(*args, **kwargs)
		return other
	return internal


@check_first_argument('pizza')
def favorite_food(*args):
	print(*args)

@check_first_argument(10)
def sum_ten(number_1, number_2):
	return number_1 + number_2


# Testando:

# print(sum_ten(10, 12))  # => 22
# print(sum_ten(1, 21))  # => Incorrect value! First value
# 					     # must be 10!

print(favorite_food("pizza", "churrasco"))
# Output:
# pizza churrasco
# None

print(15*'-')

print(favorite_food("sanduiche", "pizza"))
# Output: Incorrect value! First value must be pizza!

print(15*'-')
