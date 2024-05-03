"""
# Teste de Velocidade com Expressões Geradoras:

# Generators (Geradores):


def numbers_gen():
	for number in range(1, 10):
		yield number


ge1 = numbers_gen()
print(f"ge1: {ge1}")
# Saída - output: <generator object numbers_gen at 0x77f0b55ec5f0>

print(15*'-')

print(next(ge1))  # => 1
print(next(ge1))  # => 2
print(next(ge1))  # => 3
print(next(ge1))  # => 4
print(next(ge1))  # => 5
print(next(ge1))  # => 6
print(next(ge1))  # => 7
print(next(ge1))  # => 8
print(next(ge1))  # => 9
# print(next(ge1))  # => Error: StopIteration

print(15*'-')

# Generator Expressions:
ge2 = (number for number in range(1, 10))

print(f"ge2: {ge2}")
# Saída - output: ge2: <generator object <genexpr> at 0x714dbad268c0>

print(15*'-')

print(next(ge2))  # => 1
print(next(ge2))  # => 2
print(next(ge2))  # => 3
print(next(ge2))  # => 4
print(next(ge2))  # => 5
print(next(ge2))  # => 6
print(next(ge2))  # => 7
print(next(ge2))  # => 8
print(next(ge2))  # => 9
# print(next(ge2))  # => Error: StopIteration

print(15*'-')

# ----------------------------------------------------------

# Podemos usar as funções integradas do Python em Expressões Geradoras:

print(f"sum(number for number in range(1, 10)) = "
	  f"{sum(number for number in range(1, 10))}")


"""


import time

# Realizando o teste de velocidade:

# Para a Generator Expression:

gen_start = time.time()

print(f"sum(number for number in range(10000000)) = "
	  f"{sum(number for number in range(10000000))}")


gen_duration = time.time() - gen_start


# Para as list comprehension:

list_start = time.time()

print(f"sum(number for number in range(10000000)) = "
	  f"{sum([number for number in range(10000000)])}")

list_duration = time.time() - list_start

print("RESULTS:")
print(f"Expression Generator took {gen_duration} seconds to perform")
print(f"List Comprehension took {list_duration} seconds to perform")