"""
# Decoradores (Decorators):

* O que são decorators?
- Decorators são funções;
- Decorators envolvem outras funções e aprimoram seus
comportamentos;
- Decorators também são exemplos de Higher Order Functions;
- Decorators têm uma sintaxe própria, usando o sinal de
arroba @ (Syntatic Sugar / Açúcar Sintático).

# -----------------------------------------------------------

# Decorators como funções:
# Sintaxe não recomendada:


def be_polite(function):
	def being():
		print("It's nice to meet you!")
		function()
		print("Have a great day!")

	return being


def greeting():
	print("Welcome to Geek University!")


# Testando 1:
teste = be_polite(greeting)
teste()

print(25*'-')

# Testando 2:


def anger():
	print("I HATE YOU!")


anger_polite = be_polite(anger)
anger_polite()

print(25*'-')


# -----------------------------------------------------------


# -----------------------------------------------------------


# -----------------------------------------------------------


# -----------------------------------------------------------




"""


# Decorators com Sugar Syntax/ Açúcar Sinático (Recomendada):


def be_really_polite(function):  # => Decorator Function
	def being_really():
		print("It's nice to meet you!")
		function()
		print("Have an excellent day!")

	return being_really


@be_really_polite   # => Decorator
def presenting():
	print("My name is Pedro.")


# Testando:
presenting()

print(25*'-')

@be_really_polite
def sleep():
	print("I want to sleep...")


sleep()

print(25*'-')

# Observação: Não confundir decorator function com decorator.

