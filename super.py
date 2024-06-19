"""
# POO - O Métodos Super:

- O método super() se refere a super classe.
- Com o método super() podemos fazer acesso a qualquer
elemento da classe pai.

"""

class Animal:
	def __init__(self, name, species):
		self.__name = name
		self.__species = species

	def make_noise(self, noise):
		print(f"The {self.__name} make: {noise}")


class Cat(Animal):
	def __init__(self, name, species, breed):
		# Animal.__init__(self, name, species)
		super().__init__(name, species)
		super().make_noise("Au Au Au Au")  # => The Felix make: Au Au Au Au
		self.__breed = breed


felix = Cat('Felix', 'Felino', 'Angorá')

print(5*'_-_-')
felix.make_noise('Miau')
print(5*'_-_-')

print(15*'-')
