"""
# Trabalhando com Módulos Built-In:

- Módulos Built-In: São também chamados de 'módulos integrados', ou
seja, que já vêm instalados no interpretador do Python.

# ----------------------------------------------------

# Utilizando alias (apelidos) para módulos:

import random as rdm
print(rdm.random())

# ----------------------------------------------------

# Podemos importar todas as funções de um módulo utilizando o *:

from random import *

# Com o import acima queremos dizer: "Do módulo random, importe
# todas as funções do mesmo."

print(f'random = {random()}')

# ----------------------------------------------------------------
# importando o módulo ( t o d o o módulo) inteiro:
import random
print(f"random.random() = {random.random()}")

# ----------------------------------------------------------------

# Utilizando alias (apelidos) para funções:

from random import randint as rdi
print(f"radint(5, 89) = rdi(5,89) = {rdi(5,89)}")

# ----------------------------------------------------------------

# Utilizando alias (apelidos) para funções:

from random import randint as rdi, random as rdm

print(f"radint(5, 89) = rdi(5,89) = {rdi(5,89)}")
print(" ")
print(f"radom() = rdm() = {rdm()}")
print(" ")

# ----------------------------------------------------------------

# Índices global de módulos do Python:
https://docs.python.org/3/py-modindex.html

"""

# Costumamos utilizar tuple para colocar múltiplos import de
# um mesmo módulo:

from random import (
    random,
	randint,
	shuffle,
	choice
)

print(f"random = {random()}")
print(" ")
print(f"randint(5, 89) = {randint(5,89)}")
print(" ")
lista = ['Python', 'Geek', 'University']
shuffle(lista)
print(f"shuffle(options) = {lista}")
print(" ")
print(f"choice('University') = {choice('University')}")



