"""
# Preservando Metadata com Wraps:

# Metadata (metadados) => São dados intrínsecos aos arquivos.
# Wraps => São funções que envolvem elementos com diversas
finalidades.

# ------------------------------------------------------

# Mostrando o problema:


def ver_log(function):
	def logar(*args, **kwargs):
		'''Eu sou uma função(logar) dentro de outra.'''

		print(f"Você está chamando a função: {function.__name__}")
		print(f"Aqui a documentação: {function.__doc__}")
		return function(*args, **kwargs)
	return logar

@ver_log
def soma(a, b):
	'''Soma dois números.'''
	return a+b


# print(soma(10,30))
# Saída - output:
# Você está chamando a função: soma
# Aqui a documentação: Soma dois números.
# 40

print(f"soma.__name__ = {soma.__name__}")
print(15*'-')
print(f"soma.__doc__ = {soma.__doc__}")
print(15*'-')

# Saída - output:
# soma.__name__ = logar
# ---------------
# soma.__doc__ = Eu sou uma função(logar) dentro de outra.
# ---------------


"""

from functools import wraps
# Resolução do problema:


def ver_log(function):
	@wraps(function)
	def logar(*args, **kwargs):
		'''Eu sou uma função(logar) dentro de outra.'''

		print(f"Você está chamando a função: {function.__name__}")
		print(f"Aqui a documentação: {function.__doc__}")
		return function(*args, **kwargs)
	return logar

@ver_log
def soma(a, b):
	'''Soma dois números.'''
	return a+b


# print(soma(10,30))
# Saída - output:
# Você está chamando a função: soma
# Aqui a documentação: Soma dois números.
# 40

print(f"soma.__name__ = {soma.__name__}")
print(15*'-')
print(f"soma.__doc__ = {soma.__doc__}")
print(15*'-')

# Saída - output:
# soma.__name__ = soma
# ---------------
# soma.__doc__ = Soma dois números.
# ---------------

print("help(soma)")
print(help(soma))

# Saída - output:
# Help on function soma in module __main__:
#
# soma(a, b)
#     Soma dois números.
#
# None