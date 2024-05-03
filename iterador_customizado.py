"""
# Escrevendo um Iterador Customizado:

# Escreveremos algo semelhante ao range():

for number in range(5,11):
	print(number)


"""


# Utilizaremos o conceito de classe e atributos:

class Counter:
	def __init__(self, smaller, bigger):  # Função construtora
		self.smaller = smaller
		self.bigger = bigger

	def __iter__(self):
		return self

	def __next__(self):
		if self.smaller < self.bigger:
			number = self.smaller
			self.smaller += 1
			return number
		raise StopIteration



con = Counter(1,61)

print(f"con = {con}")
# Saída - output: con = <__main__.Counter object at 0x7f2d10ff4ad0>
print(15*'-')
print(f"con.smaller = {con.smaller}")
print(f"con.bigger = {con.bigger}")
print(15*'-')

for number in Counter(1,61):
	print(number)

