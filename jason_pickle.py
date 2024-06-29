"""
# JSON e Pickle:

JSON => JavaScript Object Notation.
API => São meios de comunicação entre os serviços
oferecidos por empresas (Twitter - X, Facebook) e
terceiros (desenvolvedores).

# -----------------------------------------------------

import json

ret = json.dumps(['product:',
                  {'PlayStation4': ('2Tb',
                                    'New',
                                    '220 V',
                                    2340)}])

print(f"type(ret) = {type(ret)}")
print(f"ret = {ret}")

# ---------------------------------------------------------

import json


class Cat:
    def __init__(self, name, breed):
        self.__name = name
        self.__breed = breed

    @property
    def name(self):
        return self.__name

    @property
    def breed(self):
        return self.__breed


felix = Cat('Felix', 'Angora')
print(f"felix.__dict__ = {felix.__dict__}")

ret = json.dumps(felix.__dict__)

print(f"ret = {ret}")


# ---------------------------------------------------------

# Integrando JSON com Pickle:

- Temos que instalar a biblioteca jsonpickel => pip install
jsonpickle.

# ---------------------------------------------------------

import jsonpickle

class Cat:
    def __init__(self, name, breed):
        self.__name = name
        self.__breed = breed

    @property
    def name(self):
        return self.__name

    @property
    def breed(self):
        return self.__breed


felix = Cat('Felix', 'Angora')

ret = jsonpickle.encode(felix)

print(ret)  # => {"py/object": "__main__.Cat",
"_Cat__name": "Felix", "_Cat__breed": "Angora"}

# ------------------------------------------------------

# Escrevendo o arquivo jason/pickle:

import jsonpickle

class Cat:
    def __init__(self, name, breed):
        self.__name = name
        self.__breed = breed

    @property
    def name(self):
        return self.__name

    @property
    def breed(self):
        return self.__breed


felix = Cat('Felix', 'Angora')

with open('felix.json', 'w') as file:
    ret = jsonpickle.encode(felix)
    file.write(ret)

# -------------------------------------------------


"""

# Lendo o arquivo jason/pickle:

import jsonpickle

class Cat:
    def __init__(self, name, breed):
        self.__name = name
        self.__breed = breed

    @property
    def name(self):
        return self.__name

    @property
    def breed(self):
        return self.__breed


with open('felix.json', 'r') as file:
    file_content = file.read()
    ret = jsonpickle.decode(file_content)
    print(f"ret = {ret}.")
    print(f"type(ret) = {type(ret)}.")
    print(f"ret.name = {ret.name}")
    print(f"ret.breed = {ret.breed}")


# Out-put:
# ret = <__main__.Cat object at 0x79f03e79fe30>.
# type(ret) = <class '__main__.Cat'>.
# ret.name = Felix
# ret.breed = Angora

