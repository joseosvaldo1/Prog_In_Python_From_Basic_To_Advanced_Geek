"""
# Conhecendo o módulo Pickle:

- A função do módulo Pickle é realizar o seguinte processo:
	* Objeto Pytho => Binarização;
	* Binarização => Objeto Python.

- O processo acima é chamado de serialização/deserialização.

Observação: O módulo Pickle não é seguro contra dados maliciosos
e, desta forma, não é recomendado trabalhar com arquivos pickle
vindo de outras pessoas que você não conheça ou de fontes
desconhecidas.



"""

import pickle

class Animal:
	def __init__(self, name):
		self.__name = name

	@property
	def name(self):
		return self.__name

	def eat(self):
		print(f"{self.__name} is eating...")


class Cat(Animal):
	def __init__(self, name):
		super().__init__(name)


	def meow(self):
		print(f"{self.name} is meowing...")


class Dog(Animal):
	def __init__(self, name):
		super().__init__(name)

	def bark(self):
		print(f"{self.name} is barking...")


felix = Cat('Felix')
pluto = Dog('Pluto')


# Fazendo a escrita em arquivos pickle:
# with open('animals.pickle', 'wb') as file:
# 	pickle.dump((felix, pluto), file)


# Fazendo a leitura de dados em arquivos pickle:
with open('animals.pickle', 'rb') as file:
	cat, dog = pickle.load(file)
	print(15 * '-')
	print(f"The cat is called: '{cat.name}'.")
	print(f"The type of cat is: '{type(cat)}'")
	cat.meow()
	print(15*'-')
	print(f"The dog is called: '{dog.name}'.")
	print(f"The type of dog is: '{type(dog)}'")
	dog.bark()
	print(15 * '-')
