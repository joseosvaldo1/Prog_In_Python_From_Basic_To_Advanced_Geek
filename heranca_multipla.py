"""
# POO - Herança Múltipla:

# Herança Múltipla nada mais é do que a possibilidade de uma
classe herdar de múltiplas classes, fazendo com que a classe
filha herde todos os atributos e métodos de todas as classes
herdadas.

Observações:

1) A herança múltipla pode ser feita de duas maneiras:
	* Por Multiderivação Direta OU;
	* Por Multiderivação Indireta.

2) Falamos que uma classe deriva de outra quando ela herda de
outra.

3) Não importa se a derivação é direta ou indireta. A classe
que realizar a herança (classe filha) herdará todos os
atributos e métodos das super classes.

# -----------------------------------------------------------

# Exemplo_1 - Multiderivação Direta:

class Base1:
	pass


class Base2:
	pass


class Base3:
	pass


class MultiDerivadaDireta(Base1, Base2, Base3):
	pass


Observação: Ocorre multiderivação direta na classe
MultiDerivadaDireta, pois a mesma herda diretamente
das classes Base1 e Base2.

# --------------------------------------------------

# Exemplo_2 - Multiderivação Indireta:

class Base1:
	pass


class Base2(Base1):
	pass


class Base3(Base2):
	pass


class MultiDerivadaIndireta(Base3):
	pass

Observação: Ocorre a multiderivação indireta na classe
MultiDerivadaIndireta, pois ela herda diretamente da Base1,
Base2 e Base3. A Base2 herda diretamente da Base1 e a Base3
herda diretamente da Base2. Dessa forma, a Base2 herda todos
os atributos e métodos da Base1, bem como a Base 3 herda
todos os atributos e métodos da Base2 e da Base1 pelo fato
de a Base2 herdá-los da Base1. Por consequência, a Base3 herda
todos os métodos e atributos das Base1 e Base2. Como a classe
MultiDerivadaIndireta herda diretamente da Base3, ela herdará
todos os métos e atributos das classes bases Base1, Base2 e
Base3.

# ---------------------------------------------------------


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


# Testing:

whale = Aquatic('Wally')
print(whale.swim())
print(whale.greeting())
print(15*'-')

armadillo = Terrestrial('Xim')
print(armadillo.walk())
print(armadillo.greeting())
print(15*'-')

penguin = Penguin('Tux')
print(penguin.walk())
print(penguin.swim())       # Method Resolution Order - MRO
print(penguin.greeting())   # => I am Tux from land. => class Penguin(Terrestrial, Aquatic):
print(15 * '-')             # => I am Tux from sea.  => class Penguin(Aquatic, Terrestrial):

# Object is an instance of ...

print(f"Tux is an instance of Animal?: {isinstance(penguin, Animal)}")  # => True
print(f"Tux is an instance of Penguin?: {isinstance(penguin, Penguin)}")  # => True
print(f"Tux is an instance of Aquatic?: {isinstance(penguin, Aquatic)}")  # => True
print(f"Tux is an instance of Terrestrial?: {isinstance(penguin, Terrestrial)}")  # => True
print(f"Tux is an instance of object?: {isinstance(penguin, object)}")  # => True

# Observação: Todas as classes em Python herdam da classe object.