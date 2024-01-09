"""
# Dir e Help:
- São utilitários que o Python disponibiliza para
auxiliar na programação.

dir -> Apresenta todos os atributos e funções/métodos
disponíveis para determinado tipo de dado ou variável.

Uso: dir(tipo de dado/variável)
Saída no console:
# Retorna todos os métodos disponíveis para um objeto
do tipo string:
>>> type('Geek')
<class 'str'>

Exemplo_1:
dir('Geek')
['__add__', '__class__', '__contains__', '__delattr__',
'__dir__', '__doc__', '__eq__', '__format__', '__ge__',
'__getattribute__', '__getitem__', '__getnewargs__',
'__getstate__', '__gt__', '__hash__', '__init__',
'__init_subclass__', '__iter__', '__le__', '__len__',
'__lt__', '__mod__', '__mul__', '__ne__', '__new__',
'__reduce__', '__reduce_ex__', '__repr__', '__rmod__',
'__rmul__', '__setattr__', '__sizeof__', '__str__',
'__subclasshook__', 'capitalize', 'casefold', 'center',
'count', 'encode', 'endswith', 'expandtabs', 'find',
'format', 'format_map', 'index', 'isalnum', 'isalpha',
'isascii', 'isdecimal', 'isdigit', 'isidentifier',
'islower', 'isnumeric', 'isprintable', 'isspace',
'istitle', 'isupper', 'join', 'ljust', 'lower',
'lstrip', 'maketrans', 'partition', 'removeprefix',
'removesuffix', 'replace', 'rfind', 'rindex', 'rjust',
'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines',
'startswith', 'strip', 'swapcase', 'title', 'translate',
'upper', 'zfill']

dir('Geek') # => 'Geek' Tipo de dado => String
'Geek'.lower() => geekdi
'Geek'.upper() => GEEK
'geek'.capitalize() => Geek

Exemplo_2:
num = 4
dir(num) # => Retorna os métodos para integers
['__abs__', '__add__', '__and__', '__bool__', '__ceil__',
'__class__', '__delattr__', '__dir__', '__divmod__',
'__doc__', '__eq__', '__float__', '__floor__',
'__floordiv__', '__format__', '__ge__',
'__getattribute__', '__getnewargs__', '__getstate__',
'__gt__', '__hash__', '__index__', '__init__',
'__init_subclass__', '__int__', '__invert__', '__le__',
'__lshift__', '__lt__', '__mod__', '__mul__', '__ne__',
'__neg__', '__new__', '__or__', '__pos__', '__pow__',
'__radd__', '__rand__', '__rdivmod__', '__reduce__',
'__reduce_ex__', '__repr__', '__rfloordiv__',
'__rlshift__', '__rmod__', '__rmul__', '__ror__',
'__round__', '__rpow__', '__rrshift__', '__rshift__',
'__rsub__', '__rtruediv__', '__rxor__', '__setattr__',
'__sizeof__', '__str__', '__sub__', '__subclasshook__',
'__truediv__', '__trunc__', '__xor__',
'as_integer_ratio', 'bit_count', 'bit_length',
'conjugate', 'denominator', 'from_bytes', 'imag',
'is_integer', 'numerator', 'real', 'to_bytes']

num = 4
type(num) => <class 'int'>
num.__abs__() => 4
num.__add__(6) => 10 (4 + 6 = 10)
(4).__add--(6) => 10


help -> Apresenta a documentação/ como utilizar os
atributos/ propriedades e funções/métodos disponíveis
para determinado tipo de dado ou variável.

Exemplo_1:
help('Geek'.lower())
Saída:
Help on built-in function lower:

lower() method of builtins.str instance
    Return a copy of the string converted to lowercase.

Observações:
1) Para usar os utilitários help e dir no terminal,
devemos abrir o interpretador do Python no mesmo.
2) Para sair do utilitário 'help', pressionamos a tecla
'q' de 'quit'.

"""

print("Dir e Help")
print("Exemplo_1:")
text = "Geek"
print(f"Tipo de 'text': {type(text)}")
print ("Dir(text) - mostra os métodos de 'text' - String:")
print(dir(text))
print("Help(text.lower():")
print(help(text.lower()))



