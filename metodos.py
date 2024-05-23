"""
# POO - Métodos:

- Métodos (funções) => Representam os comportamentos do objeto,
ou seja, as ações que este objeto pode realizar no seu sistema.

- Em Python, dividimos os métodos em dois grupos: métodos de
instância e métodos de classe.

# Métodos de Instância:

- O método dunder init (__init__) é um método especial em Python
chamado de método construtor e sua função é construir o objeto
a partir da classe.

# Observações:
1) T o d o elemento em Python que inicia e finaliza com
duplo underline (__) é chamado de Dunder (Double Underline).
2) Os métodos/funções Dunder em Python são chamado de Métodos
Mágicos.
3) Métodos devem ser escritos com letras minúsculas. Se o nome
for composto, o nome terá seus componentes separados por
underline(s) (_).
4) Só devemos criar métodos de instância, quando precisamos
acessar e/ou modificar atributos de instância.
5) Métodos de Classe em Python são conhecidos como Métodos Estáticos
em outras linguagens.

- Precisamos criar uma instância para acessar um método de
instância.



ATENÇÃO: Por mais que possamos criar nossas próprias funções
utilizando dunder, essa prática não é aconselhável. Python já
possui vários métodos com essa nomenclatura e pode ser que
mudemos o comportamento dessas funções mágicas internas da
linguagem. Então, evite ao máximo essa prática. De preferência,
nunca a faça.


"""

# Métodos de Instância => Estão vinculados a alguma instância
# da classe.

from passlib.hash import pbkdf2_sha256 as crypt

class Lamp:
	def __init__(self, color, voltage, luminosity, turn_on):
		self.__color = color
		self.__voltage = voltage
		self.__luminosity = luminosity
		self.__turn_on = False


class CurrentAccount:

	counter = 4999

	def __init__(self, limit, balance):
		self.__number = CurrentAccount.counter + 1
		self.__limit = limit
		self.__balance = balance
		CurrentAccount.counter += self.__number


class Product:
	counter = 0

	def __init__(self, id, name, description, value):
		self.__id = Product.counter + 1
		self.__name = name
		self.__description = description
		self.__value = value
		Product.counter = self.__id

	def discount(self, percentage):

		'''Returns the price of the discounted product.'''

		return (self.__value * (100 - percentage)) / 100


class User:
	# Atributos de Classe:
	counter = 0

	# Métodos de Classe:
	@classmethod
	def count_users(cls):
		print(f"Class: {cls}")
		print(f"We have {cls.counter} user(s) in the system.")

	# Método Estático em Python:
	@staticmethod
	def definition():
		return "UXR344"

	# Método Construtor da classe:
	def __init__(self, name, surname, email, password):
		self.__id = User.counter + 1
		self.__name = name
		self.__surname = surname
		self.__email = email
		self.__password = crypt.hash(password,
									 rounds=200000,
									 salt_size=16)
		User.counter = self.__id
		print(f"User created: {self.__generate_user()}")

	def check_password(self, password):
		if crypt.verify(password, self.__password):
			return True
		return False

	def __run__(self, distance): # => __run__ não é aconselhável
		print(f"{self.__name} am running {distance} meters.")

	def full_name(self):
		return f"{self.__name} {self.__surname}"

	def __generate_user(self):
		return self.__email.split('@')[0]



# ------------------------------------------------------

# p1 = Product(1, "Paystatio 4", 'Video Game', 2300.00)
# print(f"p1.price: R$ {p1.discount(10):.2f}")
# print(f"Product.discount(p1,40) = R$ {Product.discount(p1,40):.2f}")

# ------------------------------------------------------

# user_1 = User("Angelina", "Jolie",
# 			 "angelina@gmail.com", 123456)
#
# user_2 = User("Felicity", "Jones",
# 			  "felicity@gmail.com", 654321)
#
# print(f"user_1.full_name(): {user_1.full_name()}")
# print(f"User.full_name(user_1): {User.full_name(user_1)}")
# print(f"user_2.full_name(): {user_2.full_name()}")
# print(f"User.full_name(user_2): {User.full_name(user_2)}")
#
# print(15*'-')
#
# # Acesso de forma incorreta a um atributo de classe:
# print(f"user_1_password: {user_1._User__password}")
# print(f"user_2_password: {user_2._User__password}")
#
# print(15*'-')

# ------------------------------------------------------


# name = input("Enter your name: ")
# surname = input("Enter your surname: ")
# email = input("Enter your e_mail: ")
# password = input("Enter your password: ")
# confirm_password = input("Confirm your password: ")
#
# if password == confirm_password:
# 	user = User(name, surname, email, password)
# else:
# 	print("The password entered does not match.")
# 	exit(1)
#
#
# print("user created successfully!")
#
# password = input("Enter your password again: ")
#
# if user.check_password(password):
# 	print("Access allowed!")
# else:
# 	print("Access denied!")
#
# print(f"Encrypted user password: {user._User__password}")  # Acesso incorreto


# ------------------------------------------------------


# Métodos de Classe => Não estão vinculados a nenhuma instância
# da classe, mas sim diretamente a ela, porém usam um decorator
# para indicar que se trata de um método de classe.

# ------------------------------------------------------

# user = User("Felicity", "Jones",
# 			"felicity@gmail.com", "123456")
#
# User.count_users()  # => Forma Correta - Acessando pela classe
# user.count_users()  # => Forma incorreta - Acessando pela instância

# ------------------------------------------------------


# Em Python, a principal diferença entre métodos públicos e
# privados está na convenção de nomenclatura e na acessibilidade
# dos métodos dentro de uma classe e seus objetos.

# Métodos Públicos:

# Nomenclatura: Não têm nenhuma convenção especial de nomenclatura.
# São definidos normalmente, por exemplo: def metodo_publico(self):.
# Acessibilidade: Podem ser acessados e chamados de qualquer lugar,
# tanto dentro quanto fora da classe. São a forma padrão de métodos
# em Python.

# Métodos Privados:
#
# Nomenclatura: Usam uma convenção de prefixo de sublinhado duplo
# para indicar que são privados, por exemplo:
# def __metodo_privado(self):.
# Acessibilidade: Não podem ser acessados diretamente fora da classe
# devido à mangling (ofuscação) de nomes feita pelo interpretador Python.
# Isso significa que o nome do método é internamente modificado para
# incluir o nome da classe, tornando o acesso direto mais difícil. No
# entanto, ainda podem ser acessados de forma indireta ou através de
# certos mecanismos (como self._Classe__metodo_privado()), mas essa
# prática não é recomendada.
#  - Essas convenções ajudam a indicar a intenção de encapsulamento e
# de proteção dos métodos, incentivando boas práticas de programação
# orientada a objetos.



# user = User("Felicity", "Jones",
#			"felicity@gmail.com", "123456")


# print(user.__generate_user())  # => AttributeError:
# 'User' object has no attribute '__generate_user'.

# print(f"user._User__generate_user() = {user._User__generate_user()} ")
# => user._User__generate_user() = felicity => Acesso inadequado.


# Método Estáticos no Python:

# Um método estático em Python é um método que pertence a uma classe,
# mas não está associado a nenhuma instância específica dessa classe.
# Em outras palavras, ele pode ser chamado tanto na classe quanto na
# instância da classe, mas não pode acessar ou modificar o estado da
# instância (isto é, os atributos da instância).
#
# Para definir um método estático, usa-se o decorador @staticmethod
# antes da definição do método. Como métodos estáticos não dependem
# de instâncias, eles não recebem o parâmetro self como primeiro
# argumento.

# Num método estático em Python, a gente não tem acesso nem a
# classe e nem a uma instância da classe.

print(f"User.counter = {User.counter}")
print(f"User.definition() = {User.definition()}")

print(15*'-')

user = User("Felicity", "Jones",
			"felicity@gmail.com", "123456")

print(f"user.counter = {user.counter}")
print(f"user.definition() = {user.definition()}")

print(15*'-')

