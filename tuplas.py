"""
# Tuplas (tuples):

- Tuplas são bastantes parecidas com listas. Porém,
elas apresentam duas diferenças básicas:

1) As listas são representadas por parênteses - ();
2) As tuplas são IMUTÁVEIS o que siginifica que, ao
criamos uma tupla, ela não irá mudar. Toda operação
realizada em uma tupla gera uma nova tupla.

# Cuidado_1: Tuplas são representadas por parênteses,
# mas tenha cuidado, atribuição de múltiplos elementos
# usando vírgulas e sem parênteses também gera uma tupla

tuple_1 = (1, 2, 3, 4, 5, 6)
print(f"tupla 1: {tuple_1}")
print(f"type(tuple_1): {type(tuple_1)}")
print(15*'_')
tuple_2 = 1, 2, 3, 4, 5, 6
print(f"tupla 2: {tuple_2}")
print(f"type(tuple_2): {type(tuple_2)}")
print(15*'_')

# Cuidado_2: Tuplas com apenas um elemento:
tuple_3 = (4) # => Isso não é uma tupla
print(f"tupla 3: {tuple_3}")
print(f"type(tuple_3): {type(tuple_3)}")
print(15*'_')
tuple_4 = (4,) # => Isso é uma tupla
print(f"tupla 4: {tuple_4}")
print(f"type(tuple_4): {type(tuple_4)}")

# Conclusão: Podemos concluir que tuplas são definidas
# vírgula(s) e não pelos parênteses
print(" ")
print(25*"-")

(4) => Não é uma tupla. É um inteiro
(4,) => É uma tupla
4, => É uma tupla

# Podemos gerar uma tupla dinamicamente com range:
# range(inicio, fim, passo):

tuple_5 = (tuple(range(11)))
print(f"tupla 5: {tuple_5}")
print(f"type(tuple_5): {type(tuple_5)}")

print(" ")
print(25*'_')

# Desempacotamento de tuplas:
tuple_6 = ('Geek University', 'Programação em Python: Esencial')
School, Course = tuple_6

print(f"School: {School}")
print(f"Course: {Course}")

print(" ")
print(25*'_')

tuple_7 = (1, 2, 3, 4, 5, 6)
print(f"sum(tuple_7): {sum(tuple_7)}")
print(f"max(tuple_7): {max(tuple_7)}")
print(f"min(tuple_7): {min(tuple_7)}")
print(f"len(tuple_7): {len(tuple_7)}")

print(" ")
print(25*'_')

# Observações:
# 1) No desempacotamento de tuplas, ocorre um 'ValueError'
# quando o número de variáveis é diferente do número de
# elementos da tupla.

# 2) Não existem métodos de adição e remoção de elementos
# em tuplas, pois as mesmas são objetos imutáveis.

# 3) Tuplas aceitam quaisquer tipos de dados em Python.

# 4) Tuplas contendo somente objetos numéricos (int e
# float) apresentam os métodos 'sum()', 'max()', 'min()'.

# 5) Tuplas são imutáveis, mas podemos sobrescrever seus
# valores.


# Concatenação de Tuplas:

print("Priting tuple_8 and tuple_9 " +
	  "BEFORE CONCATENATION:")
tuple_8 = (1, 2, 3,)
print(f"tuple_8: {tuple_8}")
tuple_9 = (4, 5, 6,)
print(f"tuple_9: {tuple_9}")
tuple_10 = tuple_8 + tuple_9
print(f"tuple_10: {tuple_10}")
print(15*'_')
print("Priting tuple_8 and tuple_9 " +
	  "AFTER CONCATENATION:")
print(f"tuple_8: {tuple_8}")
print(f"tuple_9: {tuple_9}")

print(" ")
print(25*'_')

# Podemos sobrescrever uma tupla usando atribuição:
# tuple_8 = tuple_8 + tuple_9
# print(f"tuple_8 = {tuple_8}")
# Saída: => tuple_8 = (1, 2, 3, 4, 5, 6)

# Podemos verificar se um dado elemento está em uma
# tupla:
tuple_11 = (1, 2, 3)
print(f"tuple_11: {tuple_11}")
print(f"3 in tuple_11: {3 in tuple_11}")
print(f"4 in tuple_11: {4 in tuple_11}")

print(" ")
print(25*'_')

# Iterando sobre uma tupla:
tuple_12 = (1, 2, 3)

# 1ª Forma:
for number in tuple_12:
	print(number, end=" ")

print(15*"_")

# 2ª Forma:
for i, v in enumerate(tuple_12):
	print(f"tuple_12[{i}] = '{v}'")

print(" ")
print(25*'_')

# Contando os elementos em uma tupla:
tuple_13 = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
print(f"tuple_13 = {tuple_13}")
print(f"Count some tuple_13 elements using "
	  f"the method 'count()':")
print(f"tuple_13.count('a') = {tuple_13.count('a')}")
print(f"tuple_13.count('b') = {tuple_13.count('b')}")
print(f"tuple_13.count('c') = {tuple_13.count('c')}")

print(" ")
print(25*'_')

# Transformando string em tuplas:
school = tuple('Geek University')
print(f"school = {school}")
print(f"type(school) = {type(school)}")
print(f"school.count('e') = {school.count('e')}")

print(" ")
print(25*'_')

# Acessos a elementos de uma tupla:
# Usamos os índices começando por 0:

months = ('January', 'February', 'March', 'April','May',
		  'June', 'July', 'August','September','October',
		  'November', 'December')
print(f"months = {months}")

# Usando o 'for':
for i, v in enumerate(months):
	print(f"months[{i}] = {v}")
print(15*"_")
for i , v in enumerate(months):
	k = i + 1
	print(f"months[{k}º] = {v}")

print(" ")
print(25*'_')

# Usando o 'while':
i = 0

while i < len(months):
	print(f"months[{i}] = {months[i]}")
	i = i + 1

print(" ")
print(25*'_')

# Podemos verificar em qual índice um elemento está
# uma tupla usando o método 'index(elemento)':
print(f"months.index('June') = {months.index('June')}")
print(f"months.index('August') = {months.index('August')}")

print(" ")
print(25*'_')

# Observação: Caso o elemento não esteja na tupla,
# será retorna um erro 'ValueError' quando usarmos
# o método 'index()'.

# Dicas na utilização de tuplas:
# 1) Devemos utilizar tuplas SEMPRE que não precisarmos
# modificar os dados contidos em uma coleção:

months = ('January', 'February', 'March', 'April','May',
		  'June', 'July', 'August','September','October',
		  'November', 'December')
print(f"months = {months}")



# Slicing em Tuplas:
# tupla(inicio:fim:passo)
print(f"months[0::] = {months[0::]}")
print(f"months[5::] = {months[5::]}")
print(f"months[5:9:] = {months[5:9:]}")
print(f"months[5:9:2] = {months[5:9:2]}")
print(f"months[::-1] = {months[::-1]}")

print(" ")
print(25*'_')

# Por que usar tuplas:
# 1º Motivo: Tuplas são mais rápidas do que listas
# pelo fato de as tuplas serem imutáveis;
# 2º Motivo: Tuplas deixam seu código mais seguro,
# pois elementos imutáveis traz mais segurança
# para o código.

# Copiando uma tupla para outra:

tuple_14 = (1, 2, 3)
print(f"tuple_14 BEFORE copying "
	  f"by attribution: {tuple_14}.")

print("new_tuple_14 = tuple_14")
new_tuple_14 = tuple_14

print(f"new_tuple_14 = {new_tuple_14}")

print(15*'_')
print(f"tuple_14 AFTER copying "
	  f"by attribution: {tuple_14}.")

print(" ")
print(25*'_')

other_list = (4, 5, 6)
new_tuple_14 = tuple_14 + other_list
print(f"new_tuple_14 after 'new_tuple_14 = "
	  f"tuple_14 + other_list' = {new_tuple_14}")
print(f"tuple_14 = {tuple_14}")

print(" ")
print(25*'_')

# Observação: Nas tuplas não temos o 'shalow copy'

"""

# Dicas na utilização de tuplas:
# 1) Devemos utilizar tuplas SEMPRE que não precisarmos
# modificar os dados contidos em uma coleção:

months = ('January', 'February', 'March', 'April','May',
		  'June', 'July', 'August','September','October',
		  'November', 'December')
print(f"months = {months}")



# Slicing em Tuplas:
# tupla(inicio:fim:passo)
print(f"months[0::] = {months[0::]}")
print(f"months[5::] = {months[5::]}")
print(f"months[5:9:] = {months[5:9:]}")
print(f"months[5:9:2] = {months[5:9:2]}")
print(f"months[::-1] = {months[::-1]}")

print(" ")
print(25*'_')

# Por que usar tuplas:
# 1º Motivo: Tuplas são mais rápidas do que listas
# pelo fato de as tuplas serem imutáveis;
# 2º Motivo: Tuplas deixam seu código mais seguro,
# pois elementos imutáveis traz mais segurança
# para o código.

# Copiando uma tupla para outra:

tuple_14 = (1, 2, 3)
print(f"tuple_14 BEFORE copying "
	  f"by attribution: {tuple_14}.")

print("new_tuple_14 = tuple_14")
new_tuple_14 = tuple_14

print(f"new_tuple_14 = {new_tuple_14}")

print(15*'_')
print(f"tuple_14 AFTER copying "
	  f"by attribution: {tuple_14}.")

print(" ")
print(25*'_')

other_list = (4, 5, 6)
new_tuple_14 = tuple_14 + other_list
print(f"new_tuple_14 after 'new_tuple_14 = "
	  f"tuple_14 + other_list' = {new_tuple_14}")
print(f"tuple_14 = {tuple_14}")

print(" ")
print(25*'_')

# Observação: Nas tuplas não temos o 'shalow copy'