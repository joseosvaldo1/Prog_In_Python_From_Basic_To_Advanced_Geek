"""
# POO - Métodos Mégicos:

- Métodos mágicos são todos os métodos que utilizam
dunder (__name_do_metodo__).

- Dunder => Double Underscore (Underline) => __
- Dunder init => __init__ => Método construtor
class Book:
	def __init__(self, title, author, pages):
		self.__title = title
		self.__author = author
		self.__pages = pages

- Dunder repr => __repr__ => Representação do objeto
	def __repr__(self):
		return self.__title
		# return f"{self.__title} written by {self.__author}."


"""


class Book:
	def __init__(self, title, author, pages):
		self.__title = title
		self.__author = author
		self.__pages = pages

	def __repr__(self):
		# return self.__title
		return f"{self.__title} written by {self.__author}."

	def __str__(self):
		return self.__title

	def __len__(self):
		return self.__pages  # => Deve retornar um número inteiro.
		# return len(self.__title)

	def __del__(self):
		print("An object of type Book was deleted from memory.")

	def __add__(self, other):
		return f"{self} - {other}"

	def __mul__(self, other):
		if isinstance(other, int):
			mesage = ''
			for n in range(other):
				mesage += ' ' + str(self) 

			return mesage
		return "This operation is impossible!"



# Observação: A função do método mágico __repr__ é fazer a
# representação de um objeto.

book_1 = Book('Python Rocks', 'Geek University', 400)
book_2 = Book('AI with Python', 'Geek University', 350)

# Sem o uso do método mágico "__repr__":
# print(book_1)  # => <__main__.Book object at 0x77d6ae3f4d40>
# print(book_2)  # => <__main__.Book object at 0x77d6ae3f4d10>
#
# print(15*'-')
#
# print(str(book_1))  # => <__main__.Book object at 0x77d6ae3f4d40>
# print(str(book_2))  # => <__main__.Book object at 0x77d6ae3f4d10>
#
# print(15*'-')

# Utilizando o método mágico __repr__ com o atributo 'title':
# print(f"book_1 = {book_1}")  # => book_1 = Python Rocks
# written by Geek University.
# print(f"book_2 = {book_2}")  # => book_2 = AI with Python
# written by Geek University.

# print(15*'-')

# Utilizando o método mágico __str__ com o atributo 'title':
print(f"book_1 = {book_1}")  # => book_1 = Python Rocks
print(f"book_2 = {book_2}")  # => book_2 = AI with Python

print(15*'-')

# Diferenças entre __repr__ e __str__:

# Em Python, os métodos __repr__ e __str__ são usados para definir
# a representação de objetos como strings, mas com propósitos
# ligeiramente diferentes.

# __repr__:
# Propósito: Fornecer uma representação "oficial" da instância
# que seja mais detalhada e não ambígua, preferencialmente algo
# que possa ser usado para recriar o objeto.
# Público-alvo: Desenvolvedores e depuradores.
# Retorno: Deve retornar uma string que, idealmente, pode ser
# usada como entrada para a função eval() para recriar o objeto.
# Uso padrão: Quando você chama repr(obj) ou simplesmente escreve
# o objeto em uma sessão interativa (no REPL), o Python usa __repr__.

# __str__:
# Propósito: Fornecer uma representação informal e legível do objeto,
# que seja fácil de entender para os usuários.
# Público-alvo: Usuários finais.
# Retorno: Deve retornar uma string legível que descreve o objeto de
# uma maneira agradável.
# Uso padrão: Quando você chama str(obj) ou usa print(obj), o Python
# usa __str__.

# Observações:
# 1) Se __str__ não estiver definido, Python usará
# __repr__ como fallback. Se ambos não estiverem definidos, o
# padrão é retornar uma string contendo o tipo do objeto e o
# endereço de memória.

# 2) Quando ambos os métodos __str__ e __repr__ estão definidos,
# Python utiliza cada um no contexto apropriado:
# * __str__ para uma representação amigável ao usuário final.
# * Quando print(p) ou str(p) é chamado, o método __str__ é usado.

# * __repr__ para uma representação detalhada e útil para
# desenvolvimento e depuração.
# * Quando repr(p) é chamado ou o objeto p é simplesmente digitado
# no prompt interativo, o método __repr__ é usado.

print(f"len(book_1) = {len(book_1)}")
print(f"len(book_2) = {len(book_2)}")

print(15*'-')

print(f"book_1 + book_2 = {book_1 + book_2}")

print(15*'-')

print(f"book_1 * 2 = {book_1*2}")

print(15*'-')
