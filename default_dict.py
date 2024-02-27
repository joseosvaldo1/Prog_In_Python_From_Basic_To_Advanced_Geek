"""
# Módulo Collections - Default Dict:

link: https://docs.python.org/3/library/collections.html#collections.defaultdict

# Recapitulando Dicionários:

dict_1 = {'course': 'Programação em Python: Essencial'}

print(f"dict_1: {dict_1}")
print(15*'-')
print(f"dict_1['course']: {dict_1['course']}")
print(15*'-')
# print(f"dict_1['non-existent key']: {dict_1['non-existent key']}")
# => KeyError

print(" ")
print(25*'-')


# Default Dict: Ao criar um dicionário utilizando o 'default dict',
nós informamos um valor padrão (default value). Este valor será
utilizado sempre que não um houver um valor definido. Caso tentemos
acessar um chave inexistente, a chave será criada e o valor padrão
será atribuído a mesma.

- Lambdas: São funções sem nomes que podem ou não receber parâmetros
de entrada e retornar valores.

"""

# Fazendo o import do 'defaultdict' do módulo 'collections':
from collections import defaultdict

dict_2 = defaultdict(lambda:0)

print(" ")

# Adicionando um elemento em dict_1 -
# dict_2['curso']='Programação Em Python: Essencial'
dict_2['curso']='Programação Em Python: Essencial'
print(f"dict_2: {dict_2}")
print(15*'-')
print(f'type(dict_2): {type(dict_2)}')
print(15*'-')

print(" ")

print(15*'_')
print(f"dict_2['curso_2'] = {dict_2['curso_2']} ")
print(f"dict_2={dict_2}")