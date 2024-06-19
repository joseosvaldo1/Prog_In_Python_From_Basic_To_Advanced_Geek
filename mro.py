"""
POO - Method Resolution Order (MRO):

- Method Resolution (Resolução de Ordem do Métodos) - MRO
é a ordem de execução dos métodos (quem será executado
primeiro).
- É como a linguagem Python configura os métodos na ordem que
devem ser executados durante a instanciação do objeto das
classes.
-Em Python, a gente pode conferir a ordem da execução dos
métodos (MRO) de três formas:
	 * Via propriedade da classe __mro__;
	 * Via método mro();
	 * Via help.


"""

class Animal:
	def __init__(self, name):
		self.__name = name

	def greeting(self):
		return f"I am {self.__name}."


class Aquatic(Animal):
	def __init__(self, name):
		super().__init__(name)


	def swim(self):
		return f"{self._Animal__name} is swimming."

	def greeting(self):
		return f"I am {self._Animal__name} from sea."


class Terrestrial(Animal):
	def __init__(self, name):
		super().__init__(name)

	def walk(self):
		return f"{self._Animal__name} is walking."

	def greeting(self):
		return f"I am {self._Animal__name} from land."


class Penguin(Terrestrial, Aquatic):
	def __init__(self, name):
		super().__init__(name)

	# def greeting(self):
	# 	return f"I am a penguin!"

tux = Penguin('Tux')
print(tux.greeting())  # => I am Tux from land.
print(15 * '-')

# ----------------------------------------------

# class Penguin(Terrestrial, Aquatic): => I am Tux from land.
# class Penguin(Aquatic, Terrestrial): => I am Tux from sea.

# ----------------------------------------------

# Object is an instance of ...

print(f"Tux is an instance of Animal?: {isinstance(tux, Animal)}")  # => True
print(f"Tux is an instance of Penguin?: {isinstance(tux, Penguin)}")  # => True
print(f"Tux is an instance of Aquatic?: {isinstance(tux, Aquatic)}")  # => True
print(f"Tux is an instance of Terrestrial?: {isinstance(tux, Terrestrial)}")  # => True
print(f"Tux is an instance of object?: {isinstance(tux, object)}")  # => True

# Observação: Todas as classes em Python herdam da classe object.
