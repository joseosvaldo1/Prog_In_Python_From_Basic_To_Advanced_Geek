"""

# Sorted:

Observação: Não confunda a função sorted() com o método 'sort', pois
o 'sort' só funciona em listas.

- Podemos usar a função sorted() em qualquer iterável.
- Como o próprio nome sugere, sorted() serve para realizar ordenações.


# Exemplo_1:
print("Exemplo_1:")

numbers = (6, 1, 8, 2)

print(f"numbers: {numbers}")
print(15*'-')
print(f"sorted(numbers) = {sorted(numbers)}")
# Sorted() ordena do menor para o maior.
print(15*'-')
print(f"numbers: {numbers}")
print(15*'-')

# Observações:
# 1) O iterável original não é modificado pela função 'sorted()'.
# 2) A função 'sorted()' sempre retornará uma lista com os
# elementos do iterável ordenados.

# Exemplo_2:

# Adicionando parâmetros ao sorted():
print("Exemplo_2:")

numbers = (6, 1, 8, 2)

print(f"numbers: {numbers}")
print(15*'-')
print(f"sorted(numbers) = {sorted(numbers)}")
print(15*'-')
print(f"sorted(numbers, reverse=True) = {sorted(numbers, reverse=True)}")
# Com o parâmetro reverse=True, a função sorted() ordena do maior
# para o menor.
print(15*'-')

# Fazendo a conversão para outro tipo de iterável:
# Para uma tupla:
print(f"sorted(numbers) - tuple = {tuple(sorted(numbers))}")
# Para um conjunto set:
print(f"sorted(numbers) - set = {set(sorted(numbers))}")
print(15*'-')


# Exemplo_3:

# Podemos usar a sorted() para tarefas mais complexas:

print("Exemplo_3: ")

users = [
	{'username': 'samuel', 'tweets': ['Eu adoro bolos!', 'Eu adoro pizzas!']},
	{'username': 'carla', 'tweets': ['Eu amo meu gato']},
	{'username': 'jeff', 'tweets': []},
	{'username': 'bob123', 'tweets': [], 'color': 'yellow'},
	{'username': 'doggo', 'tweets': ['Eu gosto de cachorros!', 'Vou sair hoje']},
	{'username': 'gal', 'tweets': [], 'color': 'black', 'music': 'rock'}
]

print(f"users = {users}")
print(15*'-')
# Ordenando pelo username - ordenação alfabética:
print(f"sorted(users) = {sorted(users, key=lambda user: user['username'])}")
print(15*'-')
# Ordenando pela quantidade de tweets - da menor para a maior:
print(f"sorted(users) = {sorted(users, key=lambda user: len(user['tweets']))}")
print(15*'-')

"""

# Exemplos:

# Exemplo_4:
print("Exemplo_4: ")

songs = [
	{'title': 'Thunderstruck', 'quantity': 3},
	{'title': 'Dead Skin Mask', 'quantity': 2},
	{'title': 'Back in Black', 'quantity': 4},
	{'title': 'Too old to rock´n´roll, to young to die', 'quantity': 32},
]

# Ordena da menos para a mais tocada:
print(f"sorted(songs, key=lambda song: song['quantity']) = "
	  f"{sorted(songs, key=lambda song: song['quantity'])}'")
print(15*'-')
# Ordena da mais para a menostocada:
print(f"sorted(songs, key=lambda song: song['quantity'], reverse=True) = "
	  f"{sorted(songs, key=lambda song: song['quantity'], reverse=True)}'")

