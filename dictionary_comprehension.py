"""
# Dictionary Comprehension:

- É uma maneira concisa e eficiente de criar dicionários. Assim como as
list comprehensions, que são usadas para criar listas de forma mais
compacta, as dictionary comprehensions permitem criar dicionários de
maneira semelhante, utilizando uma única linha de código.

- A sintaxe básica de uma dictionary comprehension é a seguinte:

* {chave: valor for elemento in iterável}
* {key: value for element in iterable}

- Aqui está um exemplo simples para ilustrar como isso funciona.
Suponha que você queira criar um dicionário que mapeie os números
de 0 a 4 aos seus quadrados:


quadrados = {x: x**2 for x in range(5)}
print(quadrados)

O resultado seria:

{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

- Você também pode adicionar condições às dictionary comprehensions
para filtrar os elementos incluídos no dicionário final. Por exemplo,
se você quiser apenas os quadrados dos números pares:

quadrados_pares = {x: x**2 for x in range(5) if x % 2 == 0}
print(quadrados_pares)
O resultado seria:

{0: 0, 2: 4, 4: 16}

- As dictionary comprehensions são uma ferramenta poderosa para criar
dicionários de maneira concisa e legível, especialmente quando você
precisa transformar ou filtrar dados de maneira eficiente.

# -----------------------------------------------------------------

- Pense no seguinte:

- Se quisermos criar uma lista, fazemos:
list_1 = [1, 2, 3, 4]

- Se quisermos criar uma tupla, fazemos:
tuple_1 = (1, 2, 3, 4) # ou = 1, 2, 3, 4,

- Se quisermos criar um conjunto (set), fazemos:
set_1 = {1, 2, 3, 4}

- Se quisermos crir um dicionário, fazemos:

dict_1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Sintaxe: { chave: valor for valor in iterável}


# ---------------------------------------------------------------

# Exemplos:

# Exemplo_1:

numbers = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

square_of_numbers = {key: value**2 for key, value in numbers.items()}

print(f"numbers: {numbers}")
print(15*'-')
print(f"numbers.items() = {numbers.items()}")
print(15*'-')
print(f"square_of_numbers: {square_of_numbers}")
print(15*'-')


# Exemplo_2:
list_of_numbers = [1, 2, 3, 4, 5]
# list_of_numbers_2 = [1, 2, 3, 4, 1, 2] # => Dá o mesmo resultado de
tuple_of_numbers = (1, 2, 3, 4, 5)          # de list_of_numbers
set_of_numbers ={1, 2, 3, 4, 5}

square_of_list_of_numbers = {value: value ** 2 for value
							 in list_of_numbers}
square_of_tuple_of_numbers = {value: value ** 2 for value
							 in tuple_of_numbers}
square_of_set_of_numbers = {value: value ** 2 for value
							 in set_of_numbers}

print(f"list_of_numbers: {list_of_numbers}")
print(f"tuple_of_numbers: {tuple_of_numbers}")
print(f"set_of_numbers: {set_of_numbers}")

print(20*'-')
print(20*'-')

print(f"square_of_list_of_numbers: {square_of_list_of_numbers}")
print(15*'-')
print(f"square_of_tuple_of_numbers: {square_of_tuple_of_numbers}")
print(15*'-')
print(f"square_of_set_of_numbers: {square_of_set_of_numbers}")
print(15*'-')



# ----------------------------------------------------------

# Exemplo_3:

keys = 'abcde'
values = [1, 2, 3, 4, 5]

dict_keys_values = {keys[i]: values[i] for i in range(0, len(keys))}

print(f"dict_keys_values: {dict_keys_values}")
print(15*'-')

# ----------------------------------------------------------

"""

# Exemplos:

# Exemplo com lógica condicional:

numbers = [1, 2, 3, 4, 5]

result = {number: ('Even-Par' if number % 2 == 0 else 'Odd-Ímpar')
		  for number in numbers}

print(f"numbers = {numbers}")
print(15*'-')
print(f"result = {result}")
print(15*'-')






