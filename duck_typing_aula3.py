"""
# Checagem de Tipos em Python:
# Aula 3 - Duck Typing:
- Duck Typing é um conceito em linguagens de programação dinamicamente
tipadas, como Python, onde o tipo ou a classe de um objeto é determinado
por suas características e comportamentos (os métodos que possui) em vez
de sua herança explícita.

- O tipo ou a classe de um objeto é menos importante que os métodos
que o definem. Em vez de checar a classe ou o tipo de dado, é chacada
a presença ou não de métodos ou atributos específicos.

- Objetos similares devem ter métodos, atributos ou comportamentos
similares.

- A ideia principal do Duck Typing é: "Se parece com um pato, nada
como um pato e grasna como um pato, então é um pato". Em termos de
programação, isso significa que se um objeto implementa os métodos
esperados, ele pode ser usado no lugar de qualquer outro objeto que
implemente os mesmos métodos, independentemente de serem da mesma
classe.


"""


class BlackSwan:
	def __len__(self):
		return 42


book = BlackSwan()

print(len(book))  # => 42
print(15*'-')
name = "Geek University"
numbers_list = [12, 34, 55, 49]
names_dict = {'Carlos': 12, 'Vanessa': 34, 'Joana': 49}
print(len(name))          # => 15
print(len(numbers_list))  # => 4
print(len(names_dict))    # => 3
print(15*'-')

age = 42
weight = 81.4

# print(len(age))     # => TypeError: object of type 'int' has no len()
# print(len(weight))  # => TypeError: object of type 'float' has no len()
