"""
# Any e All:

- all(): Retorna True se todos os elementos do iterável são
verdadeiros ou se o iterável está vazio.

# Exemplos da função all():

print(f"all(): Retorna True se todos os elementos do "
	  f"iterável são verdadeiros ou se o iterável está "
	  f"vazio.")

print(f"all([0, 1, 2, 3, 4]) = {all([0, 1, 2, 3, 4])}") # => False
print(15*'-')
# O zero (0) é considerado False em Python.

print(f"all([1, 2, 3, 4]) - list = {all([1, 2, 3, 4])}") # => True
print(15*'-')
print(f"all((1, 2, 3, 4)) - tuple = {all((1, 2, 3, 4))}") # => True
print(15*'-')
print("all({1, 2, 3, 4}) - set = " + str(all({1, 2, 3, 4}))) # => True
print(15*'-')
print("all([]) - set = " + str(all([]))) # => True
print(15*'-')
print(f"all('Geek') = {all('Geek')}")
print(15*'-')

names = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']

print(f"names = {names}")
print(f"all([name[0] == 'C' for name in names]) = "
      f"{all([name[0] == 'C' for name in names])}")

print(15*'-')

# Observação: Um iterável vazio convertido em boolean resulta em
# False, porém o all() entende o mesmo como True. (all([]) = True)

print(f"all([letter for letter in 'eio' if letter in 'aeiou']) = "
      f"{all([letter for letter in 'eio' if letter in 'aeiou'])} ")

print(15*'-')


numbers = [2, 4, 10, 6, 8]
print(f"numbers = {numbers}")
print(f"[number for number in numbers if number % 2 == 0] = "
	  f"{[number for number in numbers if number % 2 == 0]}")

print(f"[number for number in numbers if number % 2 == 1] = "
	  f"{[number for number in numbers if number % 2 == 1]}")
print(15*'-')

print(f"all([number for number in numbers if number % 2 == 0]) = "
	  f"{all([number for number in numbers if number % 2 == 0])}")

print(f"all([number for number in numbers if number % 2 == 1]) = "
	  f"{all([number for number in numbers if number % 2 == 1])}")

print(15*'-')

# ---------------------------------------------------------------

- any(): Retorna True se qualquer elemento do iterável for
verdadeiro False se o iterável estiver vazio.



"""


# Exemplos da função any():

print(f"any([0, 1, 2, 3, 4]) = {any([0, 1, 2, 3, 4])}") # => True
print("any([0, False, [], (), {}]) = " +
	  str(any([0, False, [], (), {}]))) # => False

names = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
print(f"names = {names}")
print(f"any([name[0] == 'C' for name in names]) = "
      f"{any([name[0] == 'C' for name in names])}")

print(15*'-')

numbers = [2, 4, 10, 6, 8]
print(f"numbers = {numbers}")
print(f"[number for number in numbers if number % 2 == 0] = "
	  f"{[number for number in numbers if number % 2 == 0]}")

print(f"[number for number in numbers if number % 2 == 1] = "
	  f"{[number for number in numbers if number % 2 == 1]}")
print(15*'-')

print(f"any([number for number in numbers if number % 2 == 0]) = "
	  f"{any([number for number in numbers if number % 2 == 0])}")

print(f"any([number for number in numbers if number % 2 == 1]) = "
	  f"{any([number for number in numbers if number % 2 == 1])}")