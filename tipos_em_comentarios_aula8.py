"""
# Checagem de Tipos em Python:
# Aula - tipos em comentários:





"""


import math

import math


def circumference(radius):
	# type: (float) -> float  # => Type hiting em comentário.
	'''Calculate the diameter of a circle given its radius.'''
	return 2*math.pi*radius


# print(circumference(8))
# print(15*'-')
# print(circumference('Geek'))
# print(15*'-')


def header_1(text, alignment=True):
	# type: (str, bool) -> str
    if alignment:
        return f"{text.title()}\n{'-'*len(text)}"
    else:
        return f"{text.title()}".center(50, '#')


print(header_1(text='Geek University'))

print(30*'-')

print(header_1(text='Geek University', alignment=False))

print(30*'-')


def header_2(
		text,           # type: str
		alignment=True  # type: bool
             ):         # Type: (...) -> str
    if alignment:
        return f"{text.title()}\n{'-'*len(text)}"
    else:
        return f"{text.title()}".center(50, '#')


print(header_2(text='Geek University'))

print(30*'-')

print(header_2(text='Geek University', alignment=False))

print(30*'-')

# Os type hiting usando comentários também são válidos
# para nomes de variáveis e atributos de classes:

name = 'Geek University'  # type: str

