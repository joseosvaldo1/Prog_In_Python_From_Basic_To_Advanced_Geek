"""
# Conjuntos (set) em Python:

- Quando falamos em conjuntos em linguagem de programação
estamos fazendo referência a Teoria dos COnjuntos.

- Em Python, os conjuntos são chamados de 'sets'

- Sets (conjuntos) não possuem valores duplicados;

- Sets (conjuntos) não possuem valores ordenados;

- Elementos de conjuntos em Python não são acessados via índices,
ou seja, não são indexados.

- Conjuntos são indicados para se utilizar quando precisamos armazenar
elementos, mas não nos importamos com a ordenação dos mesmos. Quando
não precisamos nos preocupar com chaves, valores e índices repetidos.

- Os conjuntos(sets) são referenciados em Python por chaves - {};


* Diferenças entre dicionários e conjuntos:
1) Um dicionário tem chave/valor
   Um conjunto (set) tem apenas valor.

# Definindo um conjunto (set):
s1 = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3}) # => Repare que temos valores repetidos

print(f"s1 = {s1}")
print(f"type(s1) = {type(s1)}")

# Observação: Ao criarmos um conjunto (set), caso seja adicionado um valor
# já existente, o mesmo será ignorado sem gerar erro e não fará parte do
# conjunto (set).

print(" ")
print(25*'-')
s2 = {1, 2, 3, 4, 5, 5}
print(f"s2 = {s2}")
print(f"type(s2) = {type(s2)}")
print(" ")
print(25*'-')

# Observação: Podemos transformar uma lista e uma tupla em conjuntos.
# No entanto, as repetições que eventualmente existam nas listas e nas
# tuplas originárias não ocorrerão nos conjuntos (sets) derivados das
# mesmas.

# Podemos determinar se determinado elemento está contido
# em um dado conjunto:

if 3 in s2:
    print("s2 tem o elemento '3'!")
else:
	print("s2 não tem o elemento '3'!")

print(" ")
print(25*'-')

# Importante lembrar que, além de não termos elementos repetidos
# em um conjunto (set), não temos também ordem:

data = 99, 2, 34, 23, 2, 12, 1, 44, 5, 34

list_1 = list(data)
print(f"list_1 = {list_1}")
print(f"type(list_1) = {type(list_1)}")
print(f"len(list_1) = {len(list_1)}")
print(15*'-')

tuple_1 = tuple(data)
print(f"tuple_1= {tuple_1}")
print(f"type(tuple_1) = {type(tuple_1)}")
print(f"len(tuple_1) = {len(tuple_1)}")
print(15*'-')

# dict_1 = dict(zip(data, ['dict'] * len(data)))
dict_1 = {}.fromkeys(data,'dict')
print(f"dict_1 = {dict_1}")
print(f"type(dict_1) = {type(dict_1)}")
print(f"len(dict_1) = {len(dict_1)}")
print(15*'-')

# Observação: A função zip combina elementos de duas sequências.
# No caso, data é uma tupla e ['dict'] * len(data) é uma lista
# que contém a string 'dict' repetida o mesmo número de vezes
# que há elementos em data.

set_1 = set(data)
print(f"set_1 = {set_1}")
print(f"type(set_1) = {type(set_1)}")
print(f"len(set_1) = {len(set_1)}")
print(15*'-')

# Observações:
# 1) Listas e tuplas aceitam valores repetidos, por isso
# list_1 e tuple_1 apresentam tamanho 10 (10 elementos).
# 2) Dicionários não aceitam chaves repetidas, por isso
# o dicionário dict_1 apresenta tamanho 8 (8 elementos).
# 3) Conjuntos não aceitam repetição de valores/objetos
# contidos nos mesmos, por isso o set_1 apresenta
# tamanho 8 (8 elementos).

print(" ")
print(25*'-')

# Podemos colocar tipos de dados misturados em sets (conjuntos):
s2 = {1, 'b', True, 34.22, 44}
print(f"s2 = {s2}")
print(f"type(s2) ={type(s2)}")

# Podemos iterar em um set:
for value in s2:
	print(value)

print(" ")
print(25*'-')


# Usos interesantes com sets:
# Imagine que fizemos um formulário de visitantes em um
# feira ou museu e os visitantes informa(ram) manualmente
# a cidade de onde vieram.
# Nós adicionamos cada cidade em uma lista do Python, já
# em uma lista podemos adicionar novos elementos e ter
# repetições de elementos.

cities = ['Belo Horizonte', 'São Paulo', 'Campo Grande',
		  'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']

# Printing the elements os list 'cities':
print(f"cities = {cities}")
# Determining the number of visitors:
print(f"Number of different visitors : {len(cities)}")

print(" ")
print(25*'-')

# Agora precisamos saber o número de cidades distintas:
# Podemos passar a lista cities para função set e imprimir
# o tamanho do conjunto uma vez que ele não considera
# repetições de cidades:

print(f"Number of different cities: {len(set(cities))}")

print(" ")
print(25*'-')

# Adicionando elementos em um set(conjunto):
s3 = {1, 2, 3}
print(f"s3 BEFORE s3.add(4) = {s3}")
s3.add(4)
s3.add(4) # => Incluir um elemento existente em um set nao gera erro.
print(f"s3 AFTER s3.add(4) = {s3}")
print(" ")
print(25*'-')

# Observações:
# 1) Ao tentarmos adicionar o elemento 4 novamente ao set s3,
# não foi retornado nenhum erro. O interpretador Python ignora
# a tentativa de inclusão de elementos repetidos em um conjunto.

# Removendo elementos em um set(conjunto):
# Forma 1 - Usando o método 'remove()':
s4 = {1, 2, 3}
print(f"s4 BEFORE s4.remove(3) = {s4}")
s4.remove(3) # '3' não é índice, mas sim o valor.
# ret = s4.remove(3)
# print(f"ret = {ret}")  # => None (Nenhum valor é retornado)
print(f"s4 AFTER s4.remove(3) = {s4}")
# s4.remove(33) # '3' não é índice, mas sim o valor.
# print(f"s4 AFTER s4.remove(33) = {s4}")

# Observação: Caso o valor a ser removido com o método 'remove()'
# não seja encontrado,gerará um erro - KeyErros - apesar de conjuntos
# não serem indexados.

print(" ")
print(25*'-')

# Forma 2 - Usando o método 'discard()':
s4.discard(2)
print(f"s4 AFTER s4.discard(2) = {s4}")
s4.discard(22)
print(f"s4 AFTER s4.discard(22) = {s4}")

# Observação: Caso o valor a ser excluído do conjunto (set) usando
# o método 'discard()' não esteja contido no conjunto, nenhum erro
# será retornado.

print(" ")
print(25*'-')

# Copiando um conjunto (set) para outro:

s5 = {1, 2, 3}
print(f"s5 = {s5}")

# Forma 1 - Deep Copy - usando o método 'copy()':

new_s5 = s5.copy()

print(f"new_s5 = {new_s5}")
print(15*'-')
new_s5.add(4)
print(f"s5 AFTER new_s5.add(4) = {s5}")
print(f"new_s5 AFTER new_s5.add(4) = {new_s5}")

print(" ")
print(25*'-')

# Forma 2 - Shallow Copy - usando atribuição:

s6 = {1, 2, 3}
print(f"s6 = {s6}")

new_s6 = s6

print(f"new_s6 = {new_s6}")
print(15*'-')
new_s6.add(4)
print(f"s6 AFTER new_s6.add(4) = {s6}")
print(f"new_s6 AFTER new_s6.add(4) = {new_s6}")

print(" ")
print(25*'-')

# Podemos remover todos itens de um set(conjunto) usando
# o método 'clear()':

s7 = {1, 2, 3}
print(f"s7 = {s7}")
s7.clear()
print(f"s7 AFTER s7.clear() = {s7}")

print(" ")
print(25*'-')

# Métodos Matemáticos dos Conjuntos (sets):

# Imagine que temos dois conjuntos: Um conjunto de estudantes
# do curso de Python e o outro, do curso de Java.

students_python = {'Marcos', 'Patricia', 'Ellen',
				'Pedro', 'Júlia', 'Guilherme'}

students_java = {'Fernando', 'Gustavo', 'Júlia',
				'Ana', 'Patricia'}


# Veja que alguns alunos que estudam Python também estudam Java.
# Precimar gerar um conjunto com nomes de estudantes únicos.

# Forma 1: Utilizando o método 'union()':
studentes_unique_1 = students_python.union(students_java)
# Saída: studentes_unique_1 = {'Gustavo', 'Ana', 'Marcos',
# 'Patrícia', 'Ellen', 'Júlia', 'Pedro', 'Guilherme',
# 'Fernando', 'Patricia'}

studentes_unique_2 = students_java.union(students_python)
# Saída: studentes_unique_2 = {'Gustavo', 'Ana', 'Marcos',
# 'Patrícia', 'Ellen', 'Júlia', 'Pedro', 'Guilherme',
# 'Fernando', 'Patricia'}

print(15*'-')
print(f"studentes_unique_1 = {studentes_unique_1}")
print(15*'-')
print(f"studentes_unique_2 = {studentes_unique_2}")
print(15*'-')

# Forma 2: Utilizando o caractere pipe |:
students_uniques_3 = students_python | students_java
print(f"studentes_unique_3 = {students_uniques_3}")
print(15*'-')

print(" ")
print(25*'-')

# Precisamos gerar um conjunto de estudantes que estão
# em ambos os cursos:

# Forma 1: Usando o método 'intersection()':
students_intersec_1 = students_python.intersection(students_java)
print(f"students_intersec_1 = {students_intersec_1}")
# Saída: students_intersec_1 = {'Patricia', 'Júlia'}
print(15*'-')
students_intersec_2 = students_java.intersection(students_python)
print(f"students_intersec_2 = {students_intersec_2}")
# Saída: students_intersec_2 = {'Patricia', 'Júlia'}
print(15*'-')

print(" ")
print(25*'-')

# Forma 2: Usando o caractere do e comercial (ampersand)-&:
studentes_intersec_3 = students_python & students_java
print(f"studentes_intersec_3 = {studentes_intersec_3}")
print(15*'-')

print(" ")
print(25*'-')

"""

# Métodos Matemáticos dos Conjuntos (sets):

# Imagine que temos dois conjuntos: Um conjunto de estudantes
# do curso de Python e o outro, do curso de Java.

students_python = {'Marcos', 'Patricia', 'Ellen',
				'Pedro', 'Júlia', 'Guilherme'}

students_java = {'Fernando', 'Gustavo', 'Júlia',
				'Ana', 'Patricia'}

# Precisamos gerar um conjunto de studantes que só estejam
# em apenas em um dos dois cursos:


python_only_students = students_python.difference(students_java)
java_only_students = students_java.difference(students_python)

print(f"python_only_students = {python_only_students}")
# Saída - output: python_only_students = {'Guilherme', 'Pedro',
# 'Marcos', 'Ellen'}

print(15*'-')
print(f"java_only_students = {java_only_students}")
# Saída - output: java_only_students = {'Ana', 'Gustavo', 'Fernando'}
print(15*'-')

print(" ")
print(25*'-')

# Para conjuntos (sets) com somente elementos numéricos
# (inteiros ou floats), podemos usar max, min and sum:

s_8 = {1, 2, 3, 4, 5, 6}
print(f"Set s_8 = {s_8}")

print(f"sum(s_8) = {sum(s_8)}")
print(f"min(s_8) = {min(s_8)}")
print(f"max(s_8) = {max(s_8)}")

print(" ")
print(25*'-')