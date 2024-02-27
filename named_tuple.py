"""
# Módulo Collections - namedtuple():

link: https://docs.python.org/3/library/collections.html#collections.namedtuple

# Recapturing Tuples in Python:
tuple_1 = (1, 2, 3,)

print(15*'-')
for i in range(len(tuple_1)):
	print(f"tuple_1[{i}] = {tuple_1[i]}")

print(15*'-')
# Saída - Output:
# ---------------
# tuple_1[0] = 1
# tuple_1[1] = 2
# tuple_1[2] = 3
# ---------------

# NamedTuple: São tuplas diferenciadas onde especificando um nome
para a mesma e também parâmetros.

"""

# Importing 'namedtuple' from 'collections':
from collections import namedtuple

# We need to define the tuple name and also the parameters:

# First Mode- Declaration namedtuple - name and parameters:
# 					Name  Parameters - Separated by white space
# dog = namedtuple('dog', 'age breed name')

# Second Mode- Declaration namedtuple - name and parameters:
# 					Name  Parameters - Separated by white commas (,)
# dog = namedtuple('dog', 'age, breed, name')

# Third Mode- Declaration namedtuple - name and parameters:
# 					Name            Parameters - Within a list
dog = namedtuple('dog', ['age', 'breed', 'name'])

# Using the nametuple - dog:
ray = dog(age=2, breed='Chow Chow', name='Ray')
print(15*'-')
print(f"ray = {ray}")

# Accessing namedtuple elements:
# First Mode:

print("Accessing namedtuple elements individually: ")
print(f"ray[0] = {ray[0]}") # => Age   => 2
print(f"ray[1] = {ray[1]}") # => Breed => Chow Chow
print(f"ray[2] = {ray[2]}") # => Name  => Ray
print(15*'-')

print("Accessing namedtuple elements - iteration with 'for': ")
for i in range(len(ray)):
	print(f"ray[{i}] = {ray[i]}")
print(15*'-')
print(" ")

# Second Mode:
print("Accessing namedtuple elements - using the name of parameters: ")
print(f'ray.name = {ray.name}')
print(f'ray.age = {ray.age}')
print(f'ray.breed = {ray.breed}')
print(15*'-')

# Other methods:
print(f"ray.index = {ray.index('Chow Chow')}")
print(15*'-')
print(f"ray.count = {ray.count('Chow Chow')}")
print(15*'-')