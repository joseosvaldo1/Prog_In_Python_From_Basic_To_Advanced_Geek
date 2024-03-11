"""
# List Comprehension - Parte I:

- Utilizando 'List Comprehension' nós podemos gerar novas listas com
dados processados a partir de outro iterável.

-
- List comprehension é uma construção concisa em Python que permite
criar listas de maneira elegante e eficiente. Ela oferece uma sintaxe
mais compacta para criar listas a partir de iteráveis, como listas
existentes, strings, ou objetos iteráveis em geral.

- A estrutura básica da list comprehension em Python é a seguinte:

nova_lista = [expressao for item in iterável if condição]
Onde:

* expressao: é o valor que será incluído na nova lista.
* item: é a variável temporária que representa cada elemento do iterável.
* iteravel é a fonte de dados sobre a qual você está iterando (por exemplo,
uma lista, string, ou outro objeto iterável).
* condicao (opcional): é uma expressão booleana que determina se o item
deve ser incluído na nova lista.

- Aqui estão alguns exemplos para ilustrar a utilização de list
comprehension:

1) Criando uma lista de quadrados:

quadrados = [x**2 for x in range(1, 6)]
# Resultado: [1, 4, 9, 16, 25]

2) Filtrando elementos pares:

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [x for x in numeros if x % 2 == 0]
# Resultado: [2, 4, 6, 8, 10]

3) Convertendo uma string para uma lista de caracteres:

palavra = "python"
caracteres = [c for c in palavra]
# Resultado: ['p', 'y', 't', 'h', 'o', 'n']

4) Usando condicional para transformar elementos:

numeros = [1, 2, 3, 4, 5]
resultado = [x if x % 2 == 0 else x * 2 for x in numeros]
# Resultado: [2, 2, 6, 4, 10]

- List comprehension é uma ferramenta poderosa que permite escrever
código mais conciso e legível, evitando a necessidade de usar loops
tradicionais em muitos casos. No entanto, é importante usá-la com
moderação para garantir que o código permaneça compreensível.

# ----------------------------------------------------------------------

# Exemplos Inciais de List Comprehension:

# Exemplo_1:
numbers = [1, 2, 3, 4, 5, 6]
multiples_of_10 = [number*10 for number in numbers]

print(f"numbers = {numbers}")
print(15*'-')
print(f"multiples_of_10 = {multiples_of_10}")
print(15*'-')

# Observação: Para entender melhor o que está acontecendo devemos
# dividir a expressão em duas partes:
# 1ª parte: for number in numbers
# 2ª parte: number*10

# Exemplo_2:

half_numbers = [number/2 for number in numbers]

print(f"square_of_numbers = {half_numbers}")
print(15*'-')

# Exemplo_3:
def square(value):
	return value**2

square_of_numbers = [square(number) for number in numbers]

print(f"square_of_numbers = {square_of_numbers}")
print(15*'-')

# ----------------------------------------------------------------------

# List Comprehension versus Loop:

# Usando o loop 'for':
numbers_1 = [1, 2, 3, 4, 5]
numbers_duplicated_1 = []

for number in numbers_1:
	number_duplicated = number*2
	numbers_duplicated_1.append(number_duplicated)

print(f"numbers_duplicated_1: {numbers_duplicated_1}")
print(15*'-')

# Usando List Comprehension:
numbers_2 = [1, 2, 3, 4, 5]
numbers_duplicated_2 = [number*2 for number in numbers_2]

print(f"numbers_duplicated_2: {numbers_duplicated_2}")
print(15*'-')

# ----------------------------------------------------------------------

"""

# Outros Exemplos:

# Exemplo_1:

name = "Geek University"

print(f"name = {name}")
print(15*'-')
print(f"name.upper() = {name.upper()}")
print(15*'-')
print(f"[letter.upper() for letter in name] = "
	  f"{[letter.upper() for letter in name]}")
print(15*'-')

# Exemplo_2:

friends = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']

print(f"friends = {friends}")
print(15*'-')
print(f"[friend.upper() for friend in friends] = "
	  f"{[friend.upper() for friend in friends]}")
print(15*'-')

# Exemplo_3:

print(f"[number*3 for number in range(1,10)] = "
	  f"{[number*3 for number in range(1,10)] }")
print(15*'-')

# Exemplo_4:
print(f"[bool(value) for value in [0, [], '', True, 1, 3.14] = "
	  f"{[bool(value) for value in [0, [], '', True, 1, 3.14]]}")
print(15*'-')

# Exemplo_5:
print(f"[str(number) for number in [1, 2, 3, 4, 5]] = "
	  f"{[str(number) for number in [1, 2, 3, 4, 5]]}")
print(15*'-')