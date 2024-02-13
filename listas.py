"""
# Listas:

- Listas em Python funcionam como vetores/matrizes (arrays
em outras linguagens) com a diferença de serem DINÂMICOS e
também podermos colocar QUALQUER tipo de dados.

- Observações:
1) Dinâmicos: As listas em Python não possuem tamanho fixo,
ou seja, podemos criar a lista e ir simplesmente adicionando
os elementos.
2) Qualquer tipo de dados: As listas não possuem tipos de
dados fixos, ou seja, podemos colocar qualquer tipo de
dado.

- As listas em Python são representadas por colchetes.
- Podemos facilmente checar se um determinado valor
está contido em uma determinada lista.

# Podemos facilmente checar se um determinado valor
# está contido em uma determinada lista:

print(" ")
print(30*"-")
print("Exemplo_2:")
number = 7
if number in list_4:
    print(f"I found the number {number} in list_4!")
else:
    print(f"I didn't find the number {number} in list_4!")

print(" ")
print(30*"-")
print("Exemplo_3:")
letter = 'e'
if letter in list_5:
    print(f"I found the letter '{letter}' in list_5!")
else:
    print(f"I didn't find the letter '{letter}' in list_5")

# Podemos facilmente ordenar uma lista usando
# o método 'sort' das listas:

print("Exemplo_3:")
list_1_sorted = sorted(list_1)
print(f"list_1_sorted: {list_1_sorted}")
print(" ")
print(30*"-")
list_5_sorted = sorted(list_5)
print(f"list_5_sorted: {list_5_sorted}")
print(" ")
print(30*"-")

# Podemos facilmente contar o número de ocorrências
# de um elemento em uma lista usando o método 'count':

print("Exemplo_4:")
count_number_1 = list_1.count(1)
count_letter_e = list_5.count('e')
print(f"count_number_1: '{count_number_1}'.")
print(f"count_letter_e: '{count_letter_e}'.")
print(" ")
print(30*"-")

# Adicionar elementos em listas:


# Para adicionarmos elementos em uma lista, utilizamos a
# função 'append':
#  Observação: Com o método 'apend', só podemos adicionar
# um único elemento por vez.


print("Exemplo_5:")
print(f"list_1 BEFORE including the number 42 = "
      f"{list_1}")
list_1.append(42)
print(f"list_1 AFTER including the number 42 = "
      f"{list_1}")

print(" ")
print(30*"_")

# list_1.append(12, 34, 56) # => Gives a error
#    list_1.append(12, 34, 56)
# TypeError: list.append() takes exactly one argument
(3 given)

print(" ")
print(30*"_")

# Observação: podemos passar uma outra lista ao 'append':
list_6 = [12, 34, 56]

print(f"list_1 BEFORE including list_6 = "
      f"{list_1}")

# list_1 = list_1.append(list_6) # => Forma errada
list_1.append(list_6) # => Forma correta
# Observação: O 'append' coloca a lista como um elemento
# único (sublista).

print(f"list_1 AFTER including list_6 = "
      f"{list_1}")
print(" ")
print(30*"-")

# Observação: O 'append' coloca a lista como um elemento
# único (sublista).

print(f"list_1 AFTER including list_6 = "
      f"{list_1}")
print(" ")
print(30*"-")

# Observações:
# 1. A função append() é uma operação in-place,
# o que significa que ela modifica o próprio objeto (no
# caso, a lista list_1) em vez de retornar uma nova lista.
# Por isso, quando você faz list_1.append(list_6), a lista
# list_1 é alterada, mas o resultado da operação é None.
# 2. Para corrigir isso, você não precisa atribuir o
# resultado de append() de volta à lista. Basta chamar
# append() diretamente na lista sem atribuição. Aqui está
# a correção:

list_1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
list_6 = [12, 34, 56]

print(f"list_1 BEFORE including list_6: {list_1}")
list_1 = list_1.append(list_6) # => Forma errada
list_1.append(list_6)  # Correção aqui
print(f"list_1 AFTER including list_6: {list_1}")

Saída:
list_1 BEFORE including list_6 = [1, 99, 4, 27, 15, 22,
                                  3, 1, 44, 42, 27, 42]
list_1 AFTER including list_6 = [1, 99, 4, 27, 15, 22, 3,
                                 1, 44, 42, 27, 42,
                                 [12, 34, 56]]

if list_6 in list_1:
    print("I found the list 'list_6' in 'list_1'!")
else:
    print("I didn´t find the 'list_6' in 'list_1'!")

print(" ")
print(30*"-")
list_7 = [123, 44, 67]
list_1.extend(list_7)
print(f"list_1 AFTER extend 'list_7' = {list_1}")
print(" ")
print(30*"-")

- O método 'extend()' em listas do Python é utilizado
para adicionar elementos de uma estrutura iterável
(como uma lista, tupla, string, etc.) ao final de uma
lista existente. Ao contrário do método append(), que
adiciona um único elemento à lista, o extend() permite
adicionar vários elementos de uma vez.

- Aqui estão os detalhes sobre o método extend():

- Funcionalidade: O método extend() itera sobre o iterável
fornecido e adiciona cada elemento desse iterável ao final
da lista original.
- Modificação in-place: O método extend() modifica a lista
original, em vez de criar uma nova lista.
Exemplo:

# Exemplo de uso do método extend()
minha_lista = [1, 2, 3]
elementos_a_adicionar = [4, 5, 6]
minha_lista.extend(elementos_a_adicionar)
print(minha_lista)  # Resultado: [1, 2, 3, 4, 5, 6]

# - O elemento incluído em uma lista por meio do método
# 'append' irá sempre para a última posição da mesma.
#
# - Os elementos incluídos em uma lista por meio do método
# 'extend' irão sempra para as últimas posições da lista.
#
# Portanto, o extend() é útil quando você deseja adicionar
# vários elementos de uma vez a uma lista existente.
# Lembre-se de que ele não funciona com objetos individuais
# diretamente, mas sim com estruturas iteráveis que contêm
# esses objetos.
#
# Observação: O 'extend' coloca cada elemento da lista a
# ser incluída como um elemento adicional à lista. No
# entanto, o método 'extend' não aceita um elemento único
# que não seja iterável como, por exemplo, uma string.

# - Podemos inserir um novo elemento em uma lista inserindo
# a posição do índice com o método 'insert':
#
# - Observação: O uso do método 'insert' indicando um
# determinado índice não substitui/sobrescreve o valor
# inicial. O elemento da posição indicada no método
# 'insert' será deslocado uma posição a direita na lista.

list_1.insert(2, 'Novo Valor')
print(f"list_1 = {list_1}")

# Podemos facilmente juntar duas listas usando +:

list_8 = list_1 + list_2 # => Mesmo efeito do 'extend'
list_1.extend(list_5)
print(f"list_8 = {list_8}")
print(f"list_1 = {list_1}")
print(" ")
print(30*"-")

# Podemos facilmente obter os elementos de uma lista
# em ordem invertida usando o método 'reverse':


print("Printing list_1 and list_2 BEFORE 'reverse' method: ")
print(f"list_1={list_1}")
print(f"list_2={list_2}")

print("Printing list_1 and list_2 AFTER 'reverse' method: ")
list_1.reverse()
list_2.reverse()

# Usando os slices [::-1] obtemos o mesmo efeito
# do método 'reverse':
# print(f"list_1={list_1[::-1]}")
# print(f"list_2={list_2[::-1]}")

print(" ")
print(30*"-")

# Podemos facilmente copiar uma lista usando o
# método 'copy':
list_9 = list_2.copy()
print(f"list_9 = {list_9}")

print(" ")
print(30*"-")

# Para sabermos o tamanho de uma lista,
# usamos o método 'len':

print(f"Size of list_1 = {len(list_1)}")
print(f"Size of list_2 = {len(list_2)}")
print(f"Size of list_3 = {len(list_3)}")
print(f"Size of list_4 = {len(list_4)}")
print(f"Size of list_5 = {len(list_5)}")
print(" ")
print("Using loop 'for':")
for i in range(1, 6):
    current_list = globals()[f"list_{i}"]
    print(f"Size of list_{i} = {len(current_list)}")

print(" ")
print(30*"-")

# Podemos facilmente remover o último elemento
# de uma lista usando o método 'pop()':

print(f"List_5 BEFORE 'pop': {list_5}")
list_5.pop()
print(f"List_5 AFTER 'pop': {list_5}")
print("The method 'pop' delete the last " +
      "element of the list for default!")
print(f"List_5 BEFORE 'pop(2)': {list_5}")
print(f"List_5[2] = {list_5[2]}")
list_5.pop(2)
print(f"List_5 AFTER 'pop(2)': {list_5}")
print("The method 'pop(2) = e' delete the third " +
      "element of the list_5!")

# Observações:
# 1) O método 'pop()' não somente remove o
# último elemento como também o retorna.

# 2) Passando um número inteiro ao método 'pop()', ele
# ele retornará e excluirá o elemento correspondente
# ao índice indicado como argumento.

# 3) Os elementos a direita de 'n' em list_i(n) serão
# deslocados uma posição à esquerda depois de
# list_i.pop(n).

# 4) Se não tiver um elemento na posição 'n' em uma
# lista list_i, ocorrerá o erro "IndexError" ao fazermos
# list_i.pop(2).

print(" ")
print(30*"-")

# Podemos facilmente remover todos os elementos
# de uma lista usando o método 'clear()':
print(f"list_5 BEFORE 'clear()' = {list_5}")
list_5.clear()
print(f"list_5 AFTER 'clear()' = {list_5}")
print("The method 'clear()' deletes all " +
      "elements from the list.")

print(" ")
print(30*"-")

# Podemos facilmente repetir elementos de uma
# lista usando o operador '*':

new_list = [1, 2, 3]
print(f"new_list BEFORE new_list*3 = {new_list}")
new_list = new_list*3
print(f"new_list AFTER new_list*3 = {new_list}")

# Podemos facilmente converter uma string para uma lista
# usando o método 'split()':

# Exemplo_1:
course = "Programação em Python: Essencial"
print(f"course BEFORE using 'split()' = {course}")
course = course.split()
print(f"course AFTER using 'split()' = {course}")

# Observação: Por padrão, o método 'split()' separa
# os elementos de uma lista usando o espaço.
print(" ")
print(30*"-")

# Exemplo_2:

course_2 = "Programação,em,Python:,Essencial"
print(f"course_2 BEFORE using 'split(',')' = {course_2}")
course_2 = course_2.split(',')
print(f"course_2 AFTER using 'split(',')' = {course_2}")

# Exemplo_3:
# Podemos facilmente converter uma lista em uma string
# usando o método 'join()' indicando o separador:

list_10 = ["Programação", "Em", "Python:", "Essencial"]
# Abaixo estamos solicitando ao Python: Pegue a lista
# list_10, coloque um espaço entre cada elemento dela
# e tranforme - os em uma string

course_3 = " ".join(list_10)
print(f"course_3 = {course_3}")

# Abaixo estamos solicitando ao Python: Pegue a lista
# list_10, coloque um $ entre cada elemento dela
# e tranforme - os em uma string
course_4 = '$'.join(list_10)
print(f"course_4 = {course_4}")

print(" ")
print(30*"-")

# Podemos realmente colocar qualquer tipo de dado
# em uma lista em Python, inclusive misturando-os.

list_11 = [1, 2, 34, True, 'Geek', 'd',
           [1, 2, 3], 4534543455]
print(f"list_11 = {list_11}")
print(f"type(list_11) == {type(list_11)}")

print(" ")
print(30*"-")

# Iterando Sobre Listas:
# Exemplo_1 - Utilizando 'for':

sum = 0
for element in list_1:
    print(element, end=" ")
    sum += element

print(f"sum = {sum}")

print(" ")
print(30*"-")

# Exemplo_2 - Utilizando 'while':
shopping_cart = []
product = ''

while product != 'exit':
    print("Add a product to the list or " +
          "type 'exit' to exit")
    product = input()
    if product != 'exit':
        shopping_cart.append(product)

print("Products in shopping_cart:")
for product in shopping_cart:
    print(product)

print(" ")
print(30*"-")

# Utilizando variáveis em listas:
numbers_1 = [1, 2, 3, 4, 5]
print(f"numbers_1 = {numbers_1} ")

num_1, num_2, num_3, num_4, num_5 = 1, 2, 3, 4, 5
numbers_2 = [num_1, num_2, num_3, num_4, num_5]
print(f"numbers_2 = {numbers_2} ")
print(" ")
print(30*"-")

# Acessamos os elementos de uma lista usando índices:

# índices:  -4        -3      -2       -1  => Índices reversos
# Índices:   0         1       2        3
colors = ['green', 'yellow', 'blue', 'white']
for i in range(len(colors)):
    print(f"colors[{i}] = {colors[i]}")

# Saída:
# colors[0] = green
# colors[1] = yellow
# colors[2] = blue
# colors[3] = white

print(" ")
print(30*"-")

# Podemos acessar os elementos de uma lista usando
# indexação inversa:

for i in range(len(colors)):
    print(f"colors[{i - len(colors)}] = {colors[i - len(colors)]}")

print(" ")
print(30*"-")


# Saída:
# colors[-4] = green
# colors[-3] = yellow
# colors[-2] = blue
# colors[-1] = white

# Observação: Para simplificar o entendimento da lista,
# podemos pensar nela como um 'círculo' em que o último
# elemento está ligado ao primeiro.

# Usando os loops 'for' e 'while' em listas:

# Para o 'for':
for color in colors:
    print(color)
print(10*'-')

# Para o 'while':
index = 0
while index < len(colors):
    print(colors[index])
    index = index + 1

print(" ")
print(30*"-")

# Determinando índices usando 'for' e 'enumerate':
# Obter índice em um 'for':
for index, color in enumerate(colors):
    print("colors[" + str(index) + "] = ", color)

print(15*"-")
for index, color in enumerate(colors):
    print(index, color)

print(" ")
print(30*"-")

colors_in_list = list(enumerate(colors))
print(f"colors_in_list = {colors_in_list}")

# Saída:
# colors_in_list = [(0, 'green'), (1, 'yellow'),
#                   (2, 'blue'), (3, 'white')]

# Listas aceitam valores repetidos:
list_12 =[]
list_12.append(42)
list_12.append(42)
list_12.append(33)
list_12.append(33)
list_12.append(42)

print(f"list_12 = {list_12}")
# Saída:
# list_12 = [42, 42, 33, 33, 42]

# Métodos em listas não tão importantes, mas úteis:
# Encontrar o índice de um elemento em uma lista:
numbers = [5, 6, 7, 8, 9, 10]
# In which index of the 'numbers' list is the value 6:
print(f"numbers.index(6) = {numbers.index(6)}")
print(f"numbers[1] = {numbers[1]}")

# Saída:
# numbers.index(6) = 1
# numbers[1] = 6

print(15*'-')
# In which index of the 'numbers' list is the value 9:
print(f"numbers.index(9) = {numbers.index(9)}")
print(f"numbers[4] = {numbers[4]}")
print(15*'-')

# Saída:
# numbers.index(9) = 4
# numbers[4] = 9

# Caso não tenha um elemento em uma lista, o método
# 'index()' irá retornar um erro: 'ValueError'

# print(numbers.index(19)) => Gera um erro: 'ValueError'
# Observação: Se um elemento para o qual usarmos o método
# 'index()' tiver repetição, o método 'index()' irá
# retornar o índice do primeiro elemento encontrado.


numbers_2 = [5, 6, 7, 5, 8, 9, 10]

print(f"numbers.index(5) = {numbers.index(5)}")
print(f"numbers[0] = {numbers[0]}")

# Saída:
# numbers.index(5) = 0
# numbers[0] = 5
print(15*'-')

# Podemos fazer busca dentro de um 'range', ou seja,
# qual índice começar a buscar:

print("list.index(value, start):")
print(f" numbers_2.index(5,1) = "
      f"{numbers_2.index(5,1)}")
      # Busca o valor 5 a partir do índice 1.
print(f" numbers_2.index(5,2) = "
      f"{numbers_2.index(5,2)}")
      # Busca o valor 5 a partir do índice 2.
print(f" numbers_2.index(5,3) = "
      f"{numbers_2.index(5,3)}")
      # Busca o valor 5 a partir do índice 3.
# print(f" numbers_2.index(5,4) = "
      # f"{numbers_2.index(5,4)}") => Gera um erro
      # Busca o valor 5 a partir do índice 4. => ValueError
print(15*"-")

# Podemos fazer buscar dentro de um range indicando
# o início e o fim dos índices de busca
print("list.index(value, start, end):")
print(f" numbers_2.index(8,3,6) = "
      f"{numbers_2.index(8,3,6)}")
      # Busca o valor 8 a partir do índice 6 e até o 7.

print(" ")
print(30*"-")

# Revisão de Slicing:
# lista[inicio: fim: passo] - list[star: end: step]
# range(inicio: fim: passo) - range(star: end: step)

# Trabalhando com slice de lista com o parâmetro 'início':
list_13 = [1, 2, 3, 4]
print(f"list_13[1:] = {list_13[1:]}")
# Imprimindo todos os elementos iniciando pelo de índice 1.

print(15*"-")
print(f"list_13[2:] = {list_13[2:]}")
# Imprimindo todos os elementos iniciando pelo de índice 2.

print(15*'-')

# Trabalhando com slice de lista com o parâmetro 'fim':
list_13 = [ 1,  2,  3,  4 ]
# índices:  0   1   2   3
# ind neg: -4  -3  -2  -1

print(f"list_13[:2] = {list_13[:2]}")
# Imprimindo todos os elementos iniciando pelo de índice 0,
# indo até o elemento de índice 1 ( 2 - 1 = 1)

print(15*"-")
print(f"list_13[:4] = {list_13[:4]}")
# Imprimindo todos os elementos iniciando pelo de índice 0,
# indo até o elemento de índice 3 ( 4 - 1 = 3).
print(15*"-")

# Trabalhando com slice de lista com os parâmetros
# 'início' e 'fim':
print(f"list_13[1:3] = {list_13[1:4]}")
# Imprimindo todos os elementos iniciando pelo de índice 1,
# indo até o elemento de índice 2 ( 3 - 1 = ).

print(15*"-")
print(f"list_13[0:-1] = {list_13[0:-1]}")
# Imprimindo todos os elementos iniciando pelo de índice 0,
# indo até o elemento de índice -2 ( -1 - 1 = -2 ).

print(15*"-")
print(f"list_13[1:-1] = {list_13[1:-1]}")
# Imprimindo todos os elementos iniciando pelo de índice 1,
# indo até o elemento de índice -2 ( -1 - 1 = -2 ).
print(15*"-")

# Trabalhando com slice de lista com os parâmetros
# 'início', 'fim' e 'passo':
print(f"list_13[1::2] = {list_13[1::2]}")
# Imprimindo todos os elementos iniciando pelo de
# índice 1, indo até o elemento de índice 3 de
# 2 em 2
print(15*"-")

print(f"list_13[::2] = {list_13[::2]}")
# Imprimindo todos os elementos iniciando pelo de
# índice 0, indo até o elemento de índice 3 de
# 2 em 2

print(15*"-")

print(f"list_13[::-1] = {list_13[::-1]}")
# Imprimindo todos os elementos iniciando pelo de
# índice 3, indo até o elemento de índice 0.

print(" ")
print(30*"-")

# Invertendo valores em uma lista:
names = ['Geek', 'University']
# names[0], names[1] = names[1], names[0]
# Saída:
# ['University', 'Geek']

names.reverse()
print(names)
# Saída:
# ['University', 'Geek']

print(" ")
print(30*"-")

# Obtendo soma, valor máximo, valor mínimo e tamanho
# em listas de números inteiros ou de ponto flutuante:

numbers = [1,2,3,4,5,6]                 #    Saídas:
print(f"sum(numbers) = {sum(numbers)}") # => sum(numbers) = 21
print(f"min(numbers) = {min(numbers)}") # => min(numbers) = 1
print(f"max(numbers) = {max(numbers)}") # => max(numbers) = 6
print(f"len(numbers) = {len(numbers)}") # => len(numbers) = 6

print(" ")
print(30*"-")

# Podemos facilmente converter uma lista em uma tupla
# usando o método 'tuple()':

tuple_numbers = tuple(numbers)
print(f"tuple_numbers = {tuple(tuple_numbers)}")
print(f"type(tuple_numbers) = {type(tuple_numbers)}")
print(" ")
print(30*"-")

# Podemos fazer o desempacotamento de listas:

list_14 = [1, 2, 3]
num_1, num_2, num_3 = list_14

print(f"num_1 = {num_1}")
print(f"num_2 = {num_2}")
print(f"num_3 = {num_3}")


# Observações:
# 1) Se tivermos mais elementos para desempacotar do que
# as variáveis disponíveis, teremos um erro: ValueError;
# 2) Se tivermos menos elementos para desempacotar do que
# as variáveis disponíveis, teremos um erro: ValueError;
print(" ")
print(30*"-")


"""

print("---------Listas---------")
print("Exemplo_1:")
list_1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
list_2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v',
        'e', 'r', 's', 'i', 't', 'y']
list_3 = []
list_4 = list(range(11))
list_5 = list("Geek University")

print(f"list_1 = {list_1} ")
print(f"list_2 = {list_2} ")
print(f"list_3 = {list_3} ")
print(f"list_4 = {list_4} ")
print(f"list_5 = {list_5} ")
print(" ")
print(30*"-")

# Copiando uma lista para outros -
# Shallow Copy and Deep Copy:

# Forma 1 - Deep Copy:
list_15 = [1, 2, 3]
print(f"list_15 = {list_15} ")
new_list_15 = list_15.copy()
print(f"new_list_15 BEFORE append(4) = {new_list_15} ")
new_list_15.append(4)
print(f"new_list_15 AFTER append(4) = {new_list_15} ")
print(15*'_')
print(f"list_15 = {list_15} ")
print(f"new_list_15 = {new_list_15} ")
print(" ")
print(30*"-")

# Veja que, ao usarmos list_15.copy() copiamos os dados da
# list_15 para uma nova lista (new_list_15), mas ambas são
# totalmente indepedentes uma da outra, ou seja, modificando
# uma lista não afetamos a outra. Isto em Python é chamado
# de Deep Copy - Cópia Profunda.

# Forma 2 - Shallow Copy:
list_16 = [1, 2, 3]
new_list_16 = list_16

print(15*'_')
print("Printing list_16 e new_list_16 BEFORE "
      "append(4) in new_list_16:")
print(f"list_16 = {list_16} ")
print(f"new_list_16 = {new_list_16} ")
print(15*'_')
print("Printing list_16 e new_list_16 AFTER "
      "append(4) in new_list_16:")

new_list_16.append(4)
print(f"list_16 = {list_16} ")
print(f"new_list_16 = {new_list_16} ")

# Veja que utilizamos a cópia via atribuição e copiamos
# os dados de uma lista para outra. No entanto, após
# realizarmos a mudança na nova lista copiada por
# atribuição, a alteração na mesma refletiu-se em ambas
# as listas. Isto em Python é chamado de Shallow Copy.