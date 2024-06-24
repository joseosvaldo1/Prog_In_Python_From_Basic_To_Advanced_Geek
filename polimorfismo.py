"""
POO - Polimorfismo:

Poli (do grego) => Muito(s)/muita(s)
Morfis (do grego) => Formas

- Quando falamos de polimorfismo, estamos falando de objetos que
podem possuir muitas formas, ou melhor, se comportar de formas
diferentes.

- Quando a gente reimplementa um método presente na classe
pai em classes filhas, estamos realizando uma sobrescrita de
método (Overriding).

- O overriding é a melhor representação (essência) do
polimorfismo.

"""


class Animal(object):
	def __init__(self, name):
		self.__name = name

	def talk(self):
		mesage_error = 'The child class needs to implement this method.'
		raise NotImplementedError(mesage_error)

	def eat(self):
		print(f"{self.__name} is eating...")


class Dog(Animal):
	def __init__(self, name):
		super().__init__(name)


	def talk(self):
		print(f"{self._Animal__name} talk 'au au'.")


class Cat(Animal):
	def __init__(self, name):
		super().__init__(name)

	def talk(self):
		print(f"{self._Animal__name} talk 'miau'.")


class Rat(Animal):
	def __init__(self, name):
		super().__init__(name)

	def talk(self):
		print(f"{self._Animal__name} is talking something...")


# Testes:
felix = Cat('Felix')
felix.talk()
felix.eat()

print(15*'-')

pluto = Dog('Pluto')
pluto.talk()
pluto.eat()

print(15*'-')

mickey = Rat('Mickey')
mickey.eat()
mickey.talk()

print(15*'-')
