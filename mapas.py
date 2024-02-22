"""
# Mapas => Conhecidos em Python como Dicionários.

- Dicionários em Python são representado

# Iterando sobre dicionários:
incomes = {'jan': 100, 'feb': 120, 'mar': 300}
print(f"incomes = {incomes}")
print(f"type(incomes) = {type(incomes)}")
print(15*'-')

print("Keys - Chaves em incomes:")
for key in incomes:
	print(key)

print(15*'-')

print("Values - Valores em incomes:")
for key in incomes:
	print(incomes[key])

print(15*'-')

print("Keys and Values - Valores e Chaves em incomes:")
for key in incomes:
	print(f"Em {key} recebi R$ {incomes[key]}")

# Acessando as chaves em um dicionário:
# Determinando as chaves usando o método 'keys()':
print(f"Keys in incomes: {incomes.keys()}")
print(15*'-')

for key in incomes.keys():
	print(f"incomes[{key}] = {incomes[key]}")

# Acessando os valores em um dicionário:
print(f"incomes.values() = {incomes.values()}")

print(15*'-')
for value in incomes.values():
	print(value)

# Desempacotamento de dicionários:

for key, value in incomes.items():
	print(f"key = {key} and value = {value}")

print(f"incomes.item = {incomes.items()}")

"""

# Iterando sobre dicionários:
incomes = {'jan': 100, 'feb': 120, 'mar': 300}
print(f"incomes = {incomes}")
print(f"type(incomes) = {type(incomes)}")
print(15*'-')


# Métodos usados quando temos valores numéricos:
print(f"sum(incomes.values()) = {sum(incomes.values())}")
print(f"max(incomes.values() = {max(incomes.values())}")
print(f"min(incomes.values() = {min(incomes.values())}")
print(f"len(incomes)= {len(incomes)}")

print(15*'-')

