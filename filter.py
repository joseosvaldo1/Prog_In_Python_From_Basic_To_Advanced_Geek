"""
# Filter:

- Em Python, filter() é uma função embutida que permite filtrar elementos
de um iterável (como uma lista, tupla, conjunto, etc.) com base em uma
função de filtragem especificada. A função de filtragem é aplicada a
cada elemento do iterável e, se a função retornar True para esse
elemento, ele será incluído no resultado; caso contrário, será excluído.

- A sintaxe básica do filter() é a seguinte:

              filter(função_de_filtragem, iterável)

* função_de_filtragem: Esta é a função que define o critério de filtragem.
Ela deve retornar True ou False para cada elemento do iterável.
* iterável: Este é o iterável do qual os elementos serão filtrados.
Por exemplo, suponha que temos uma lista de números e queremos filtrar
apenas os números pares:

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def eh_par(numero):
    return numero % 2 == 0

pares = filter(eh_par, numeros)

print(list(pares))  # Saída: [2, 4, 6, 8, 10]

- Neste exemplo, a função eh_par() retorna True se o número for par e
False caso contrário. Então, quando aplicamos filter() com essa função
à lista de números, apenas os números pares são incluídos no resultado.

- É importante notar que filter() retorna um iterador em Python 3.x.
Portanto, geralmente usamos list() para converter o iterador resultante
de volta em uma lista.

# -----------------------------------------------------------------

- Filter: Serve para filtrar dados em Python em uma determinada coleção.

import statistics

# statistics -> é uma biblioteca para trabalhar com
# dados estatísticos.


# Exemplos:

# Exemplo_1:

values = (1, 2, 3, 4, 5, 6)

avarage_values = sum(values) / len(values)

print(f'avarage_values = {avarage_values:.1f}')

def over_avarage_values(value):
	if value > avarage_values:
		return True


over_avarage = list(filter(over_avarage_values, values))
print(f'over_avarage_values = {over_avarage}')
print(15*'-')

# Exemplo_2:

# Dados coletados de algum sensor:
data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados coletados com a função mean():
# mean => média aritimética

avarage_data = statistics.mean(data)
print(f"average_data = {avarage_data:.2f}")


# Observação: Assim como a função 'map()', a função filter() recebe dois
# parâmetros: uma função e um iterável.

over_avarage_data = list(filter(lambda value: value > avarage_data, data))
bellow_avarage_data = list(filter(lambda value: value < avarage_data, data))

print(f"over_avarage_data = {over_avarage_data}")
print(f"bellow_avarage_data = {bellow_avarage_data}")
print(15*'-')

# Observação: O 'filter object' retornado pela função filter()
# será um iterável e, por isso, o qual será completamente esgotado
# na primeira chamada do mesmo.

# Exemplo_3:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_even(number):
	return number % 2 == 0


pair_numbers = filter(is_even, numbers)

print(f"type(pair_numbers) = {type(pair_numbers)}")
print(f"pair_numbers = {list(pair_numbers)}")  # Saída: [2, 4, 6, 8, 10]
print(f"pair_numbers_again = {list(pair_numbers)}")  # Saída: []

print(15*'-')

# ----------------------------------------------------------

# Exemplo_4:

# Remoção de dados faltantes:

countries = ['', 'Argentina', '', 'Brasil','Chile', '', 'Colombia',
			 '', 'Equador', '', '', 'Venezuela']

# Em ciência de dados, não é interessante fazer qualquer processamento de
# dados em geral com dados faltantes. Dessa forma, devemos inicialmente
# realizar a filtragem e retirada dos dados faltantes.

countries_filtered = list(filter(None, countries))
# Motivo: '' is None == False
# countries_filtered = list(filter(lambda country: country != '', countries))
# countries_filtered = list(filter(lambda country: len(country) > 0, countries))

print(f"countries_filtered = {countries_filtered}")

# -----------------------------------------------------

# A diferença básica entre as funções map() e filter() é:

# A função map(): Recebe dois parâmetros, uma função e um iterável, e
# retorna um objeto (iterável) mapeando a função para cada elemento do
# iterável.

# A função filter(): Recebe dois parâmetros, uma função e um iterável, e
# retorna um objeto (iterável) filtrando apenas de acordo com a função a
# qual sempre retornará um valor booleando (True ou Falso) que fará com
# que um dado seja ou não selecionado.

# -----------------------------------------------------------------

# Exemplo_5:

users = [
	{'username': 'samuel', 'tweets': ['Eu adoro bolos!', 'Eu adoro pizzas!']},
	{'username': 'carla', 'tweets': ['Eu amo meu gato']},
	{'username': 'jeff', 'tweets': []},
	{'username': 'bob123', 'tweets': []},
	{'username': 'doggo', 'tweets': ['Eu gosto de cachorros!', 'Vou sair hoje']},
	{'username': 'gal', 'tweets': []}
]

print(f"users = {users}")
print(15*'-')

# Filtrar os usuários que estão inativos no Twitter (X):

# Forma_1:
# inactive_users = list(filter(lambda user: len(user['tweets']) == 0, users))

# Forma_2:
# inactive_users = list(filter(lambda user: user['tweets'] == [], users))

# Forma_3:
inactive_users = list(filter(lambda user: not user['tweets'], users))
# Motivo: [] is False => False => not(False) = True
# bool([]) = False => bool(not([])) = True

print(f"inactive_users = {inactive_users}")
print(15*'-')

# ---------------------------------------------------------------

"""

# Exemplo_5:

# Como combinar filter() e map():

names = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contento a seguinte expressão:
# "Sua instrutora é " + name, desde que cada nome tenha
# menos de 5 caracteres.

list_names = list(map(lambda name: f"Sua instrutora é {name}",
				  filter(lambda name: len(name) < 5, names)))

print(f"list_names = {list_names}")