"""
# Módulo Collections - Ordered Dicit:

link: https://docs.python.org/3/library/collections.html#collections.OrderedDict

- Em Python, um OrderedDict é um tipo de estrutura de dados que é
semelhante a um dicionário padrão (dict), mas com a distinção
importante de que mantém a ordem de inserção dos elementos.
Isso significa que, ao iterar sobre as chaves e valores de um
OrderedDict, a ordem será a mesma em que os itens foram adicionados
ao dicionário.

- A partir do Python 3.7, a manutenção da ordem de inserção tornou-se
uma característica padrão dos dicionários na linguagem. Isso significa
que em versões mais recentes do Python (3.7 e acima), os dicionários
comuns também mantêm a ordem de inserção. Antes disso, a ordem dos
elementos em um dicionário não era garantida.


# Dicionários comuns:
# Em um dicionário comum, a ordem de inserção não é garantida:

dict_1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

print(f"dict_1: {dict_1}")

print(" ")

for key, value in dict_1.items():
	print(f"chave = {key} => valor = {value}")

"""

# Fazendo o import do 'OrderdDict' de 'collections':
from collections import OrderedDict

dict_2 = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
for key, value in dict_2.items():
	print(f"chave = {key} => valor = {value}")

print(" ")
# Entendendo a diferença entre dict e OrderedDict:

# Dicionários Comuns em Python:
dict_3 = {'a': 1, 'b': 2}
dict_4 = {'b': 2, 'a': 1}

print(15*'-')
print(f"dict_3 == dict_4 => {dict_3 == dict_4}")
# Saída: True => a ordem dos elementos não importa para o dicionário.

print(" ")
print(f"dict_3 = {dict_3}")
print(f"dict_4 = {dict_4}")

print(15*'-')
print(" ")

# OrderedDict em Python:
ordered_dict_3 = OrderedDict(dict_3)
ordered_dict_4 = OrderedDict(dict_4)
print(15*'-')
print(f"ordered_dict_3 == ordered_dict_4 => {ordered_dict_3 == ordered_dict_4}")
# Saída: False => a ordem dos elementos importa para o OrderedDict.
print(" ")
print(f"ordered_dict_3 = {ordered_dict_3}")
print(f"ordered_dict_4 = {ordered_dict_4}")
print(15*'-')
print(" ")