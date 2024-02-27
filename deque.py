"""
# Módulo Collections - Deque:

link: https://docs.python.org/3/library/collections.html#collections.deque

- Podemos dizer que o 'dequer' é uma lista de alta performance.

- Em Python, o deque (abreviação de "double-ended queue" ou fila
de dupla extremidade) é uma estrutura de dados que permite a inserção
e remoção eficientes de elementos tanto no início quanto no final da
fila. Ele está disponível no módulo collections. O deque é semelhante
a uma lista, mas oferece operações de inserção e remoção mais eficientes
em ambas as extremidades, enquanto as listas em Python são mais eficientes
para operações de inserção/remoção no final.


"""
# Realizando a importação da biblioteca 'deque' de 'collections':
from collections import deque

# Criando deques:

d_1 = deque('Geek')

print(f"d_1 = {d_1} ")
print(f"type(d_1) = {type(d_1)}")
print(15*'-')


d_1.append('y') # => Adiciona um elemento ao final da lista.
print(f"d_1 BEFORE append('y') = {d_1} ")

d_1.appendleft('K') # => Adiciona um elemento ao início da lista.
print(f"d_1 BEFORE appendleft('K') = {d_1} ")
print(15*'-')
print(" ")

# Removendo elementos:


d_1.pop() # => Remove e retorna o último elemento da lista
print(f"d_1 BEFORE d_.pop() = {d_1}")
d_1.popleft() # => Remove e retorna o primeiro elemento da lista
print(f"d_1 BEFORE d_.popleft() = {d_1}")
print(15*'-')