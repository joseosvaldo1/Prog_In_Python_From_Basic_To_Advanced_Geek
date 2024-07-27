"""
# Checagens de Tipos em Python:
# Aula 6 - Fazendo uso de annotations:

- Annotations (anotações) em Python são metadados opcionais que você
pode adicionar às declarações de funções, variáveis e classes para indicar
os tipos esperados. Elas foram introduzidas no Python 3.0 e são amplamente
usadas em conjunto com ferramentas de verificação de tipo, como MyPy, para
melhorar a legibilidade do código e fornecer informações sobre os tipos
esperados.

# -----------------------------------------------------------------

def header(text: str, alignment: bool = True) -> str:
    if alignment:
        return f"{text.title()}\n{'-'*len(text)}"
    else:
        return f"{text.title()}".center(50, '#')


print(header(text='Geek University'))

print(30*'-')

print(header(text='Geek University', alignment=False))

print(30*'-')

print(header(text='Geek University', alignment=True))

print(30*'-')

print(header(text = '4', alignment = True))


# Observações:

# Forma correta do uso do annotation em type hiting:
# Para parâmetros:
# nome_do_parâmetro: tipo_do_dado_do_parametro  OU
# nome_do_parâmetro: tipo_do_dado_do_parametro = valor_inicial_do_parametro

# text: str  => Forma correta
# alignment: bool = True  => Forma correta


# Para o retorno de funções:

#def name_da_funcao(parâmetros) -> tipo_de_dado_do_retorno_da_funcao:

# def header(text: str, alignment: bool = True) -> str:


# Forma incorretas do uso de annotatios em type hiting:

# Para os parâmetros:

# text:str   => Forma incorreta
# text : str => Forma incorreta

# alignment:bool = True  => Forma incorreta
# alignment:bool= True  => Forma incorreta
# alignment:bool =True  => Forma incorreta
# alignment:bool=True  => Forma incorreta
# alignment : bool= True  => Forma incorreta

# Para os retornos de função:

# def header(text: str, alignment: bool = True)->str:  => Forma incorreta
# def header(text: str, alignment: bool = True)-> str: => Forma incorreta
# def header(text: str, alignment: bool = True) ->str: => Forma incorreta


# -----------------------------------------------------------------



# -----------------------------------------------------------------



"""


# Podemos facilmente verificar e conhecer as annotations
# usadas pelos nossos componentes de programação:


import math


def circumference(radius: float) -> float:
	'''Calculate the diameter of a circle given its radius.'''
	return 2*math.pi*radius


# print("circumference().__annotations__:")
# print(circumference.__annotations__)  # => {'radius': <class 'float'>,
# 'return': <class 'float'>}

# Podemos usar annotatios para outros componentes como
# variáveis, atributos, etc:

name: str = 'Geek University'
weight: float = 67.9
active: bool = True
print(15*'-')

print(name)
print(weight)
print(active)

print(15*'-')

globals_variables = __annotations__

print(globals_variables)  # => {'name': <class 'str'>, 'weight':
# <class 'float'>, 'active': <class 'bool'>}

class Person:
	def __init__(self, name: str, age: int, weight: float) -> None:
		self.__name: str = name
		self.__age :int = age
		self.__weight: float = weight
	
	def walk(self) -> str:
		return f"{self.__name} is walking."

print(15*'-')

p = Person(name='Geek University', age=37, weight=69.5)

print(f"p.__dict__ = {p.__dict__}")  # => p.__dict__ = {'_Person__name':
# 'Geek University', '_Person__age': 37, '_Person__weight': 69.5}
print(15*'-')

# print(f"p.__dannotations__ = {p.__annotations__}")  # => AttributeError:
# 'Person' object has no attribute '__annotations__'

print(f"p.walk.__annotations = {p.walk.__annotations__}")  # => '{return':
# <class 'str'>}
print(15*'-')

print(f"p.__init__.__annotations = {p.__init__.__annotations__}")  # =>
# {'name': <class 'str'>, 'age': <class 'int'>, 'weight': <class 'float'>,
# 'return': None}

print(15*'-')
