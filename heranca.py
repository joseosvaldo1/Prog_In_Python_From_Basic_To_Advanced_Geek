"""
# POO - Herança (Inheritance):

- A idéia de herança corresponde a reaproveitar código. Também
extender nossas classes.

Observações:

1) Com a herança, a partir de uma classe existente (classe pai), nós
extendemos outra classe (classe filha) que passa a herdar atributos
e métodos da classe herdada (classe pai).

- Suponhamos os clientes e os usuários de um banco:

Clientes:
    * nome;
    * sobrenome;
    * cpf;
    * renda.

Funcionários:
    * name;
    * sobrenome;
    * cpf;
    * matrícula.



# Observações:
1) Quando uma classe herda de outra classe, ela herdará t o d o s
os atributos e métodos da classe herdada.
2) Quando uma classe herda de outra classe, a classe herdada é
conhecida por:
	[Person]
	* Super Classe;
	* Classe Mãe;
	* Classe Pai,
	* Classe Base
	* Classe Genérica.
3) Quando uma classe herda de outra, ela é conhecida por:
	[Client, Employee]
	* Sub Classe;
	* Classe Filha;
	* Classe Específica.

# ------------------------------------------------------------


class Person:

	def __init__(self, name, surname, cpf):
		self.__name = name
		self.__surname = surname
		self.__cpf = cpf

	def full_name(self):
		return f"{self.__name} {self.__surname}"


class Client(Person):
	'''Client inherits from Person.'''

	def __init__(self, name, surname, cpf, income):
		# Forma não comum de acessar dados da superclasse
		Person.__init__(self, name, surname, cpf)
		self.__income = income


class Employee(Person):
	''' Employee inherits from Person. '''
	def __init__(self, name, surname, cpf, registration):
		# Forma comum de acessar dados da super classe.
		super().__init__(name, surname, cpf)
		self.__registration = registration




client1 = Client('Angelina', 'Jolie',
                 '123.456.789-99', 5000.00)

employee1 = Employee('Felicity', 'Jones',
                     '987.654.321-11', 1234 )
print(15*'-')
print(f"client1.full_name() = {client1.full_name()}")
print(f"employee1.full_name() = {employee1.full_name()}")
print(15*'-')

print("Verificando os dicts dos objetos acima:")
print(f"client1.__dict__ = {client1.__dict__}")
print(f"employee1.__dict__ = {employee1.__dict__}")

print(15*'-')

# ---------------------------------------------------

# Sobrescrita de Métodos (Overriding):

- Sobrescrita de método ocorre quando reescrevemos/reimplementamos
um método presente na super classe em classes filhas.




"""


class Person:

	def __init__(self, name, surname, cpf):
		self.__name = name
		self.__surname = surname
		self.__cpf = cpf

	def full_name(self):
		return f"{self.__name} {self.__surname}"


class Client(Person):
	'''Client inherits from Person.'''

	def __init__(self, name, surname, cpf, income):
		# Forma não comum de acessar dados da superclasse
		Person.__init__(self, name, surname, cpf)
		self.__income = income


class Employee(Person):
	''' Employee inherits from Person. '''
	def __init__(self, name, surname, cpf, registration):
		# Forma comum de acessar dados da super classe.
		super().__init__(name, surname, cpf)
		self.__registration = registration

	def full_name(self):
		print(15*'=')
		print(f"super().full_name = {super().full_name()}")
		print(f"super()._Person__cpf = {self._Person__cpf}")
		print(15*'=')
		return (f"Employee: {self.__registration} - "
		        f"Name: {self._Person__name} "
		        f"{self._Person__surname}")


client1 = Client('Angelina', 'Jolie',
                 '123.456.789-99', 5000.00)

employee1 = Employee('Felicity', 'Jones',
                     '987.654.321-11', 1234 )


print(15*'-')
print(f"client1.full_name() = {client1.full_name()}")
print(f"employee1.full_name() = {employee1.full_name()}")
print(15*'-')





