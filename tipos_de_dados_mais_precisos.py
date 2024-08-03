"""
# Novos Recursos do Python:

- Tipos de Dados Mais Precisos:


# ---------------------------------------------------------


def duplicate(value: int) -> int:
	return 2*value


print(duplicate(8))
print(duplicate(42))

# ----------------------------------------------------------

# Literal Type:

- O tipo Literal permite especificar que uma variável deve ter um
valor específico, proporcionando uma maneira de restringir valores
possíveis.

# Exemplos:

# from typing import Literal
#
#
# code_page1 = 200
# code_page2 = 404
# code_page3 = 202
#
#
# def get_status_1(code: Literal[200, 404]) -> str:
# 	if code == 200:
# 		return "OK"
# 	elif code == 404:
# 		return "Not Found"
#
#
# print(get_status_1(code_page1))  # => OK
# print(get_status_1(code_page2))  # => Not Found
# print(get_status_1(code_page3))  # => None

# ---------------------------------------------------------------

def get_status_2(user: str) -> Literal['connected', 'disconnected']:
	pass

# ---------------------------------------------------------------

def calculate_v1(operation: str, number1: int, number2: int) -> None:
	if operation == "+":
		print(f'{number1} + {number2} = {number1 + number2}')
	elif operation == "-":
		print(f'{number1} - {number2} = {number1 - number2}')
	else:
		raise ValueError(f'Invalid operation: {operation!r}')


calculate_v1('+',6, 4)
calculate_v1('-', 10, 2)
calculate_v1('*', 3, 5)

# -----------------------------------------------------------------------


def calculate_v2(operation: Literal['+','-'], number1: int, number2: int) -> None:
	if operation == "+":
		print(f'{number1} + {number2} = {number1 + number2}')
	elif operation == "-":
		print(f'{number1} - {number2} = {number1 - number2}')
	else:
		raise ValueError(f'Invalid operation: {operation!r}')


calculate_v2('+',6, 4)
calculate_v2('-', 10, 2)
calculate_v2('*', 3, 5)

# ------------------------------------------------------------------

# Union Type:

- No Python, o tipo Union é usado para indicar que uma variável, parâmetro
de função ou valor de retorno pode ser de mais de um tipo. É uma ferramenta
poderosa na tipagem estática, que permite especificar múltiplos tipos
possíveis para uma única variável, aumentando a flexibilidade enquanto
mantém a verificação de tipos.


# Exemplo:

from typing import Union


def sum(number1: int, number2: int) -> Union[str, int]:
	result: int = number1 + number2
	if result > 50:
		return f"The value {result} is very large!"
	else:
		return result


print(sum(2, 23))
print(15*'-')
print(sum(10, 41))
print(15*'-')

# Verificação usando o MyPy:

(guppe) jose@jose:~/PycharmProjects/guppe/guppe
/Prog_In_Python_From_Basic_To_Advanced_Geek$ mypy
tipos_de_dados_mais_precisos.py
tipos_de_dados_mais_precisos.py:82: error: Argument 1 to
"calculate_v2" has incompatible type "Literal['*']"; expected
"Literal['+', '-']"  [arg-type]
Found 1 error in 1 file (checked 1 source file)



# ------------------------------------------------------------------


# Final Type:


- O Final permite indicar que um nome (seja uma variável ou uma classe)
não deve ser redefinido ou herdado.

- O Final pode ser usado para expressar constantes.

# Exemplos:

from typing import Final

NAME: Final = 'Geek'

print(NAME)  # => Geek

print(15*'-')

NAME = 'University'

print(NAME)  # => University

print(15*'-')

# Verificação usando o MyPy:
# (guppe) jose@jose:~/PycharmProjects/guppe/guppe/
# Prog_In_Python_From_Basic_To_Advanced_Geek$
# mypy tipos_de_dados_mais_precisos.py
# tipos_de_dados_mais_precisos.py:135: error: Cannot assign
# to final name "NAME"  [misc]
# Found 1 error in 1 file (checked 1 source file)


# ---------------------------------------------------------------------

# Existe o decorador 'final' com f minúsculo:

@final
class Person:
	pass


class Student(Person):
	pass


	@final
	def study(self):
		print('I am studying...')


class Trainee(Student):
	pass


	def study(self):
		print('I am studying and I am interning...')


# Fazendo a verificação com o MyPy:
# (guppe) jose@jose:~/PycharmProjects/guppe/guppe/
# Prog_In_Python_From_Basic_To_Advanced_Geek$ mypy
# tipos_de_dados_mais_precisos.py
# tipos_de_dados_mais_precisos.py:175: error: Cannot inherit from
# final class "Person"  [misc]
# tipos_de_dados_mais_precisos.py:184: error: Cannot inherit from
# final class "Person"  [misc]
# tipos_de_dados_mais_precisos.py:188: error: Cannot override final
# attribute "study" (previously declared in base class "Student")  [misc]
# Found 3 errors in 1 file (checked 1 source file)



# ---------------------------------------------------------------------


# Typed Dict:

- O TypedDict permite definir dicionários cujas chaves têm tipos
específicos associados a elas. É particularmente útil para verificar
tipos em estruturas de dados que são dicionários.

from typing import TypedDict


class PythonCourse(TypedDict):
	version: str
	update: int


geek = PythonCourse(version='3.8.5', update=2020)
print(geek)  # => {'version': '3.8.5', 'update': 2020}
print(type(geek))  # => <class 'dict'>

print(15*'-')

other = PythonCourse(anything='vai', thing=True)
print(other)
print(type(other))  # => <class 'dict'>

print(15*'-')

# Fazendo a verificação com MyPy:
# (guppe) jose@jose:~/PycharmProjects/guppe/guppe/
# Prog_In_Python_From_Basic_To_Advanced_Geek$ mypy
# tipos_de_dados_mais_precisos.py
# tipos_de_dados_mais_precisos.py:251: error: Missing keys
# ("version", "update") for TypedDict "PythonCourse"
# [typeddict-item]
# tipos_de_dados_mais_precisos.py:251: error: Extra keys
# ("anything", "thing") for TypedDict "PythonCourse"
# [typeddict-unknown-key]
# Found 2 errors in 1 file (checked 1 source file)


# ---------------------------------------------------------------------

# Protocol:

- O tipo de dado Protocol foi introduzido no Python 3.8 no módulo typing.
Ele permite a definição de interfaces estruturais, também conhecidas como
duck typing. Com Protocol, é possível definir classes que especificam um
conjunto de métodos e propriedades que outras classes devem implementar,
sem necessidade de herança direta.







# ---------------------------------------------------------------------








# ---------------------------------------------------------------------

"""

# Protocol:

from typing import Protocol


class Course(Protocol):
	title: str = "Python Programming"
	

def study(value: Course) -> None:
	print(f"I am studying the course: '{value.title}'.")


class Sale:
	title = 'Oi'
	


v1 = Sale()
# c1 = Course()  # => Protocol não pode ser instanciado

study(v1)
# study(c1)  # => Protocol não pode ser instanciado








	















