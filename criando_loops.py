"""
# Criando sua própria versão de loops:

# --------------------------------------------------------

# Exemplos iniciais de for:
numbers = [1, 2, 3, 4, 5, 6]
for number in numbers:
	print(number, end=' ')    # => 1 2 3 4 5 6

print("\n")

print(15*'-')

name = "Geek University"

for letter in name:
	print(letter, end=' ')   # => G e e k   U n i v e r s i t y

print("\n")

print(15*'-')

# --------------------------------------------------------

"""

def my_for(iterable):
	'''A for loop created using iter() and next()'''
	iterator = iter(iterable)
	while True:
		try:
			print(next(iterator))
			
		except StopIteration:
			break


name = 'Geek University'
my_for(name)

print(15*'-')

numbers = [1, 2, 3, 4, 5, 6]
my_for(numbers)

print(15*'-')


