"""
# POO - Objetos:

Objetos => São instancias da classe, ou seja, após o mapeamento do
objeto do mundo real para a sua representação computacional, devemos
poder criar quantos objetos forem necessários. Podemos pensar nos
objetos/instâncias de uma classe como variáveis do tipo definido na
classe.

# -----------------------------------------------------------------


class Lamp:
	# Método Construtor em Python => __init__
	def __init__(self, color, voltage, luminosity):
		self.__color = color
		self.__voltage = voltage
		self.__luminosity = luminosity
		self.__turn_on = False

	def check_lamp(self):
		return self.__turn_on

	def turn(self):
		if self.__turn_on:
			self.__turn_on = False
		else:
			self.__turn_on = True

		return self.__turn_on

class CurrentAccount:

	counter = 4999

	def __init__(self, limit, balance):
		self.__number = CurrentAccount.counter + 1
		self.__limit = limit
		self.__balance = balance
		CurrentAccount.counter += self.__number


class User:
	def __init__(self, name, surname, email, password):
		self.__name = name
		self.__surname = surname
		self.__email = email
		self.__password = password



# Instâncias / Objetos:
lamp1 = Lamp("White", 110, 60)
lamp1.turn()

print(f"The lamp is turn on: {lamp1.check_lamp()}")


cc1 = CurrentAccount(5000, 20000)
user1 = User('Felicity', 'Jones',
			 'felicity@gmail.com', '123456')


# -----------------------------------------------------------------


name_1 = 'Angelina'
surname_1 = 'Jolie'
email_1 = 'angelina@gmail.com'
password_1 = '123456'

user_1 = User(name_1, surname_1, email_1, password_1)

print(f"user_1 = {user_1}")  # => user_1 = <__main__.User
# object at 0x72e1fcaf2240>
print(f"str(user_1) = {str(user_1)}")  # => str(user_1) =
# <__main__.User object at 0x72e1fcaf2240>
print(f"repr(user_1) = {repr(user_1)}")  # => repr(user_1) =
# <__main__.User object at 0x73fc86af2480>
print(f"type(user_1) = {type(user_1)}")  # => type(user_1) =
# <class '__main__.User'>


# -----------------------------------------------------------



"""

class Lamp:
	# Método Construtor em Python => __init__
	def __init__(self, color, voltage, luminosity):
		self.__color = color
		self.__voltage = voltage
		self.__luminosity = luminosity
		self.__turn_on = False

	def check_lamp(self):
		return self.__turn_on

	def turn(self):
		if self.__turn_on:
			self.__turn_on = False
		else:
			self.__turn_on = True

		return self.__turn_on


class Client:
	def __init__(self, name, cpf):
		self.__name = name
		self.__cpf = cpf

	def say_hi(self):
		print(f"The client {self.__name} say 'hi'")


class CurrentAccount:

	counter = 4999

	def __init__(self, limit, balance, client):
		self.__number = CurrentAccount.counter + 1
		self.__limit = limit
		self.__balance = balance
		self.__client = client
		CurrentAccount.counter += self.__number

	def show_client(self):
		print(f"The client is {self.__client._Client__name}.")
		# return f"The client is {self.__client._Client__name}."

class User:
	def __init__(self, name, surname, email, password):
		self.__name = name
		self.__surname = surname
		self.__email = email
		self.__password = password



# Instâncias / Objetos:

# lamp = Lamp()  # => TypeError: Lamp.__init__() missing
# 3 required positional arguments: 'color', 'voltage',
# and 'luminosity'

# cc = CurrentAccount()  # => TypeError: CurrentAccount.__init__()
# missing 2 required positional arguments: 'limit' and 'balance'

# user = User()  # => TypeError: User.__init__() missing
# 4 required positional arguments: 'name', 'surname', 'email',
# and 'password'

# Observação: Durante a instanciação de um objeto, devemos
# informar todos os parâmetros obrigatórios do mesmo.


cli_1 = Client('Angelina Jolie', '123.456.789-99')

cc1 = CurrentAccount(5000, 10000, cli_1)
cc1.show_client()

cc1._CurrentAccount__client.say_hi()  # => Acesso inadequado



