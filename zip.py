"""
# Zip:

- zip(): Cria um iterável (Zip Object) que agrega elementos de cada
um dos iteráveis passados como entrada em pares.


# Exemplos:

print("Exemplo_1:")
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

zip_1 = zip(list_1, list_2, 'abc')

print(f"zip_1 = {zip_1}")  # => zip_1 = <zip object at 0x7bc039503500>
print(15*'-')
print(f"type(zip_1) = {type(zip_1)}")  # => type(zip_1) = <class 'zip'>
print(15*"-")

# Sempre poderemos gerar uma lista, tupla ou set ou dicionário
# usando um Zip Object:

print(f"list(zip_1) = {list(zip_1)}")
print(15*'-')

zip_1 = zip(list_1, list_2, 'abc')
print(f"tuple(zip_1) = {tuple(zip_1)}")
print(15*'-')

zip_1 = zip(list_1, list_2, 'abc')
print(f"set(zip_1) = {set(zip_1)}")
print(15*'-')

zip_1 = zip(list_1, list_2)
print(f"dict(zip_1) = {dict(zip_1)}")
print(15*'-')


# Observação: Na conversão para dicionário, o Zip Object deve ter exatamente
# dois argumentos, pois formará um dicionário com as chaves do primeiro
# associando os elementos do segundo como valores.

print("Exemplo_2: ")

list_3 = [7, 8, 9, 10, 11]
zip_2 = zip(list_1, list_2, list_3)
print(f"list(zip_2) = {list(zip_2)}")
# Saída: list(zip_2) = [(1, 4, 7), (2, 5, 8), (3, 6, 9)]


# Observação: A função zip() utiliza como parâmetro o menor tamanho em
# iterável. Isto significa que se estiver trabalhando com iteráveis de
# tamanhos diferentes, irá parar quando os elementos do menor iterável
# acabar.

# -----------------------------------------------------------------

# Podemos utilizar diferentes iteráveis com a função zip():

tupla = (1, 2, 3, 4, 5)
lista = [6, 7, 8, 9, 10]
dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}

zt = zip(tupla, lista, dicionario.values())

print(f"list(zt) = {list(zt)}")
# Saída: list(zt) = [(1, 6, 11), (2, 7, 12), (3, 8, 13), (4, 9, 14),
# (5, 10, 15)]
print(15*'-')

# Lista de Tuplas:

data = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]

print(f"list(zip(*data)) = {list(zip(*data))}")

print(15*'-')

# ------------------------------------------------------------

"""


# Exemplos mais complexos:

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['maria', 'pedro', 'carla']

final = {data[0]: max(data[1], data[2]) for data
         in zip(alunos, prova1, prova2)}

print(f"zip(alunos, prova1, prova2) = {list(zip(alunos, prova1, prova2))}")
print(f"final = {final}")
print(15*'-')

# Podemos utilizar a função map() para resolver
# a situação anterior:

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))

print(f"dict(final) = {dict(final)}")
print(15*'-')


