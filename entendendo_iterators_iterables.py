"""
# Entendo Iterators e Iterables:

- Iterator:
	* É um objeto que pode ser iterado;
	* Um objeto que retorna um dado, sendo um elemento por vez,
	quando a função 'next()' for chamada.

- Iterable:
	* É um objeto que irá retornar um iterator quando a função
	'iter()' for chamada.


# ---------------------------------------------------------

- Em Python, tanto iteradores quanto iteráveis são conceitos
fundamentais relacionados à iteração sobre objetos em uma
sequência. Aqui estão as diferenças principais:

1. Iterável (Iterable):
- Um objeto é considerado iterável se puder ser percorrido item
por item.
- Os iteráveis são objetos que possuem um método __iter__() ou
__getitem__() implementado.
- Exemplos comuns de iteráveis incluem listas, tuplas, strings,
dicionários e conjuntos.

2. Iterador (Iterator):
- Um iterador é um objeto que permite a iteração sobre um iterável.
- Um iterador mantém um estado interno e sabe como acessar os elementos
subsequentes em um iterável.
- Os iteradores implementam os métodos __iter__() e __next__().
- Quando todos os elementos de um iterável são percorridos, o iterador
levanta uma exceção StopIteration.
- Exemplos de iteradores incluem objetos retornados por iter(iterable)
e geradores criados usando funções geradoras (yield). Em resumo, um
iterável é um objeto que pode ser percorrido, enquanto um iterador é
o objeto que efetivamente realiza a iteração sobre esse iterável.
Um iterador mantém o estado da iteração e sabe como obter o próximo
elemento do iterável.


# ---------------------------------------------------------------

name = "Geek"                 # =>  é um iterale, mas não é um iterator
numbers = [1, 2, 3, 4, 5, 6]  # =>  é um iterale, mas não é um iterator

print(f"name = {name}")        # => name = Geek
print(f"numbers = {numbers}")  # => numbers = [1, 2, 3, 4, 5, 6]

print(15*'-')

# Usando a função next() diretamente em name e numbers:
# print(next(name))   # => TypeError: 'str' object is not an iterator
# print(next(numbers))  # => TypeError: 'list' object is not an iterator


# Transformando os iterables em interator usando a função 'iter()':
iter_name = iter(name)
iter_numbers = iter(numbers)

# Usando a função next() em iter_name e iter_number:
# Para iter_name:
print('Geek:')
print(next(iter_name))  # => G
print(next(iter_name))  # => e
print(next(iter_name))  # => e
print(next(iter_name))  # => k
# print(next(iter_name))  # => StopIteration

print(15*'-')

# Para iter_numbers:
print(numbers)
print(next(iter_numbers))  # => 1
print(next(iter_numbers))  # => 2
print(next(iter_numbers))  # => 3
print(next(iter_numbers))  # => 4
print(next(iter_numbers))  # => 5
print(next(iter_numbers))  # => 6
# print(next(iter_numbers)) => StopIteration

print(15*'-')

"""

name = "Geek"

for letter in name:
	print(letter)

# No 'for' acima, o interpretador Python está passando o iterable
# name como argumento da função 'iter()'. Em seguida, ele passa
# cada elemento de iter(name) para a função 'next()'. Por último,
# ele exibe cada retorno da função next() usando a função print().