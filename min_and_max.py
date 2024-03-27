"""
# Min e Max:

* max(): Retornar o maior valor em um iterável ou o maior valor de
de dois ou mais elementos.

# Exemplos - max():

list_of_numbers = [1, 8, 4, 99, 84, 129]

print(f"list_of_numbers = {list_of_numbers}")
print(15*'-')
print(f"max(list_of_numbers) = {max(list_of_numbers)}")  # => 129
print(25*'-')

tuple_of_number = (1, 8, 4, 99, 84, 129)

print(f"tuple_of_number = {tuple_of_number}")
print(15*'-')
print(f"max(tuple_of_number) = {max(tuple_of_number)}")  # => 129
print(25*'-')

set_of_number = {1, 8, 4, 99, 84, 129}

print(f"set_of_number = {set_of_number}")
print(15*'-')
print(f"max(set_of_number) = {max(set_of_number)}")  # => 129
print(25*'-')

dict_of_number = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 84, 'f': 129}

print(f"dict_of_number = {dict_of_number}")
print(15*'-')
print(f"max(dict_of_number) = {max(dict_of_number)}")  # => f
print(f"max(dict_of_number).values() = "
	  f"{max(dict_of_number.values())}")   # => 129
print(25*'-')

print(f"max(3, 34) = {max(3, 34)}")

print(15*'-')


# Faça um programa que receba dois valores de um usuário e o maior:

value_1 = float(input("Enter the first value: "))
value_2 = float(input("Enter the second value: "))
print(" ")
print(15*'-')
print(f"The biggest value is: {max(value_1, value_2)}")
print(15*'-')

# Exemplos diversos sobre max():

print(f"max(4, 67, 54) = {max(4, 67, 54)}")
print(15*'-')
print(f"max('a','ab', 'abc') = {max('a', 'ab', 'abc')}")
print(15*'-')
print(f"max('a', 'b', 'c', 'g') = {max('a', 'b', 'c', 'g')}")
print(15*'-')
print(f"max(3.145, 5.789) = {max(3.145, 5.79)}")
print(15*'-')
print(f"max('Geek University') = {max('Geek University')}")

# ----------------------------------------------------------

* min(): Retorna o menor valor em um iterável ou menor de dois
ou mais elementos.

# Exemplos - min():

list_of_numbers = [1, 8, 4, 99, 84, 129]

print(f"list_of_numbers = {list_of_numbers}")
print(15*'-')
print(f"min(list_of_numbers) = {min(list_of_numbers)}")  # => 1
print(25*'-')

tuple_of_number = (1, 8, 4, 99, 84, 129)

print(f"tuple_of_number = {tuple_of_number}")
print(15*'-')
print(f"min(tuple_of_number) = {min(tuple_of_number)}")  # => 1
print(25*'-')

set_of_number = {1, 8, 4, 99, 84, 129}

print(f"set_of_number = {set_of_number}")
print(15*'-')
print(f"min(set_of_number) = {min(set_of_number)}")  # => 1
print(25*'-')

dict_of_number = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 84, 'f': 129}

print(f"dict_of_number = {dict_of_number}")
print(15*'-')
print(f"min(dict_of_number) = {min(dict_of_number)}")  # => a
print(f"min(dict_of_number).values() = "
	  f"{min(dict_of_number.values())}")   # => 1
print(25*'-')

print(f"min(3, 34) = {min(3, 34)}")  # => 3

print(15*'-')


# Faça um programa que receba dois valores de um usuário e o menor:

value_1 = float(input("Enter the first value: "))
value_2 = float(input("Enter the second value: "))
print(" ")
print(15*'-')
print(f"The smallest value is: {min(value_1, value_2)}")
print(15*'-')

# Exemplos diversos sobre min():

print(f"min(4, 67, 54) = {min(4, 67, 54)}")
print(15*'-')
print(f"min('a','ab', 'abc') = {min('a', 'ab', 'abc')}")
print(15*'-')
print(f"min('a', 'b', 'c', 'g') = {min('a', 'b', 'c', 'g')}")
print(15*'-')
print(f"min(3.145, 5.789) = {min(3.145, 5.79)}")
print(15*'-')
print(f"min('Geek University') = {min('Geek University')}")
print(15*'-')

# ----------------------------------------------------------

# Outros Exemplos:

names = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']
print(f"names = {names}")
print(15*'-')

print(f"max(names) = {max(names)}")  # => Tim
print(15*'-')

print(f"min(names) = {min(names)}")  # => Arya
print(15*'-')

print(f"max(names, key=lambda name: len(name)) = "
	  f"{max(names, key=lambda name: len(name))}")  #  => Ollivander

print(15*'-')

print(f"min(names, key=lambda name: len(name)) = "
	  f"{min(names, key=lambda name: len(name))}")  # => Tim

print(15*'-')

# ----------------------------------------------------------

"""

songs = [
	{'title': 'Thunderstruck', 'quantity': 3},
	{'title': 'Dead Skin Mask', 'quantity': 2},
	{'title': 'Back in Black', 'quantity': 4},
	{'title': 'Too old to rock´n´roll, to young to die', 'quantity': 32},
]

print(f"max(songs, key=lambda song: song['quantity']) = "
	  f"{max(songs, key=lambda song: song['quantity'])}")

print(15*'-')

print(f"min(songs, key=lambda song: song['quantity']) = "
	  f"{min(songs, key=lambda song: song['quantity'])}")

print(15*'-')

# Desafio_1: Imprima apenas o título da música mais e menos tocadas:

print(f"max(songs, key=lambda song: song['quantity'])['tile'] = "
	  f"{max(songs, key=lambda song: song['quantity'])['title']}")

print(15*'-')

print(f"min(songs, key=lambda song: song['quantity'])['tile'] = "
	  f"{min(songs, key=lambda song: song['quantity'])['title']}")

print(15*'-')

# Desafio_2: Como encontrar a música mais e a menos tocada
# sem usar max(), min() e lambda:

max = 0
for song in songs:
	if song['quantity'] > max:
		max = song['quantity']

for song in songs:
	if song['quantity'] == max:
		print(f"Música mais tocada = {song['title']}")


min = 999

for song in songs:
	if song['quantity'] < min:
		min = song['quantity']


for song in songs:
	if song['quantity'] == min:
		print(f"Música menos tocada = {song['title']}")