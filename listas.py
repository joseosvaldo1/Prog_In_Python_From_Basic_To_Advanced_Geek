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