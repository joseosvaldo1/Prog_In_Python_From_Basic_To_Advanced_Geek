"""
# Teste de Uso de Memória Usando Generators:

- Sequencia de Fibonacci: 1, 1, 2, 3, 5, 8, 13, ...


# -------------------------------------------------------

def fib_list(max):
	numbers = []
	a, b = 0, 1
	while len(numbers) < max:
		numbers.append(b)
		a, b = b, a + b

	return numbers


for number in fib_list(20500):
	print(number)


# teste 1 => 24.9 MB de memória para 20500 números da seq de Fibonacci.


"""


# Fazendo uma função para gerar a sequencia de Fibonacci:

def fib_list(max):
	numbers = []
	a, b = 0, 1
	while len(numbers) < max:
		numbers.append(b)
		a, b = b, a + b

	return numbers


def fib_generator(max):
	a, b, counter = 0, 1, 0
	while counter < max:
		a, b = b, a + b
		yield a
		counter = counter + 1


for number in fib_generator(20500):
	print(number)

# teste 2 - 4.6 MB de memória para 20500 números da seq de Fibonacci.


