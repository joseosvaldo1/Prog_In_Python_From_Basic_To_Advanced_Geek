"""
# Módulo Collections - Counter:

- Collections => High-Performance Container Datetypes
- O módulo collections em Python fornece alternativas
especializadas e eficientes para os tipos de contêineres
incorporados, como listas, tuplas, conjuntos e dicionários.
Ele inclui várias classes que são úteis para tarefas
específicas e oferecem melhor desempenho em comparação
com as implementações padrão. Abaixo estão algumas das
classes notáveis fornecidas pelo módulo collections:

# Counter:

- A classe Counter é usada para contar a ocorrência de
elementos em uma sequência. Ela retorna um dicionário
com os elementos como chaves e as contagens como valores.

- Counter recebe um objeto iterável como parâmetro e
retorna um objeto do tipo Collection Counter que é
parecido com um dicionário, contendo como chave um
elemento do iterável passado como parâmetro e como
valor a quantidade de ocorrência desse elemento.


# Exemplo_1:
print("Exemplo_1:")
# Podemos usar qualquer iterável, no caso uma lista(list_1):
list_1 = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4,
		  4, 5, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]


# Utilizando o Counter:
result = Counter(list_1)


print(f"result = {result}")
# Saída - Output: result = Counter({1: 5, 3: 5, 2: 4, 5: 4, 4: 3,
# 						           45: 2, 66: 2, 43: 1, 34: 1})
print(15*'-')
print(f"type(result) = {type(result)}")
# Saída - Output: type(result) = <class 'collections.Counter'>
print(15*'-')

# Veja que, para cada elemento da lista, o Counter criou uma chave
# com o elemento e, como valor, a quantidade de ocorrências.

print(" ")
print(25*'-')

# Exemplo_2:
print("Exemplo_2:")
course = "Geek University"

course_counter = Counter(course)
print(f"course_counter = {course_counter}")
# Saída - Output:
# course_counter = Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1,
# ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})

"""

# Realizando a importação da biblioteca 'Counter' de 'collections':
from collections import Counter

# Exemplo_3:
print("Exemplo_3:")

large_text = """Sir Valston Eldridge Hancock KBE, CB, DFC 
(31 de maio de 1907 – 29 de setembro de 1998) foi um oficial 
da Real  Força Aérea Australiana (RAAF) que chegou à patente 
de marechal do ar e serviu como Chefe do Estado-Maior da 
Aeronáutica de 1961 a 1965. Formado pelo Real Colégio 
Militar, Hancock foi transferido do Exército para a RAAF 
em 1929 e qualificou-se como piloto. A sua formação 
administrativa em Duntroon levou-o a ocupar principalmente 
cargos de estado-maior, incluindo vice-diretor de operações
e inteligência na sede da RAAF de 1931 a 1935 e diretor de 
obras e edifícios de 1937 a 1939."""

# Gerando uma lista de palavras por meio do método split():

word_list = large_text.split()

result = Counter(word_list)

print(f"result = {result}")

# Determinando as 5 palavras mais frequentes em word_list:
print(f"5 most frequent words = {result.most_common(5)} ")

