"""
# Dicionários em Python:


- Em alguma linguagens de programação, os dicionários em Python são
conhcidos como mapas.

- Dicionários em Python são coleções do tipo chave/valor.

- Dicionários são representados por chaves - {}.

- A separação entre chave e valor correspondentes são separados por
dois pontos (:) => chave:valor

- Tanto a chave quanto o valor em dicionários podem ser de qualquer
tipo de dado.

- Podemos misturar os tipos de dados nos dicionários.

- Dicionários em Python não são indexados.

- Para acessar um elemento da lista de um dicionario, devemos usar
a chave do elemento: => dicionario[chave_do_elemento]

- dicionario[chave_do_elemento] = valor_do_elemento

- Se tentarmos acessar um elemento usando uma chave que não exista,
será retornado um erro: 'KeyError'

- Caso o método 'get()' não encontre o objeto com a chave informada,
será retornado o valor 'None' e não será gerado o 'KeyError'.

- Podemos definir um valor padrão para quando não tivermos uma chave
um dicionário quando usarmos o método 'get()': dict_1.get('key',
default_value).


print("Dictionaries in Python:")

# Criação de dicionários:
# 1ª Forma:

print("Creating dictionaries:")
print("First way - using dict_1 = {key1:value1, key2:value2, ...}:")
countries = {'br': 'Brazil',
			 'usa': 'United States of America',
			 'py': 'Paraguay'}

print(f"countries = {countries}")
print(15*"-")
print(f"type(countries) = {type(countries)}")

print(25*"-")
print(" ")

# 2ª Forma:
print("Second way - using dict_2 = dict(key1=value1, key2=value2, ...):")
countries_2 = dict(br="Brazil", usa="United States of America", py="Paraguay")

print(f"countries_2 = {countries_2}")
print(15*"-")
print(f"type(countries_2) = {type(countries_2)}")

print(25*"-")
print(" ")

# Acessando Elementos em Dicionários:
print(" ")
print("1ª Forma: Usando as Chaves:")
print("1st Way: Usaning Keys:")
print("Acessando Elementos em Dicionários:")
countries = {'br': 'Brazil',
			 'usa': 'United States of America',
			 'py': 'Paraguay'}

print(15*'-')

print("Acessando os elementos de forma individual:")
print(f"countries['br'] = {countries['br']}")
print(f"countries['usa'] = {countries['usa']}")
print(f"countries['py'] = {countries['py']}")
# print(f"countries['ru'] = {countries['ru']}") => KeyError: 'ru'

print(25*"-")
print(" ")

print(f"Acessando os elementos usando iteração com 'for':")
for k, v in countries.items():
	print(f"countries[{k}] = {v}")

print(15*'-')

print("2ª Forma: Usando o Método 'get()':")
print("2nd Way: Usaning The Method 'get()':")
print("Acessando os elementos de forma individual:")
print(f"countries.get('br') = {countries.get('br')}")
print(f"countries.get('usa') = {countries.get('usa')}")
print(f"countries.get('py') = {countries.get('py')}")
print(f"countries.get('ru') = {countries.get('ru')}") # => None

print(15*'-')

# Incluindo Elementos em Dicionários:

print("Incluindo Elementos em Dicionários:")

countries = {'br': 'Brazil',
			 'usa': 'United States of America',
			 'py': 'Paraguay'}

russia = countries.get('ru')
country_1 = countries.get('py')


print(15*'-')
print(f"countries = {countries}")
print(15*'-')
print(f"russia = {russia}")
print(f"country_1 = {country_1}")
print(15*'-')

# Caso o método 'get()' não encontre o objeto com a chave informada,
# será retornado o valor 'None' e não será gerado o 'KeyError'.

if russia:
	print(f"Encontrei o país:")
	print(f"I found the country:")
else:
	print(f"Não encontrei o país.")
	print(f"I didn´t find the country.")

print(15*'-')

if country_1:
	print(f"Encontrei o país: '{country_1}'.")
	print(f"I found the country.")
else:
	print(f"Não encontrei o país")
	print(f"I didn´t find the country.")

print(15*'-')

country_2 = countries.get('pt', 'Country didn´t find!')
print(f"País procurado usando a chave 'pt': '{country_2}'.")
print(f"Country searched using the key 'pt': '{country_2}'.")
# - Podemos definir um valor padrão para quando não tivermos uma
# chave um dicionário quando usarmos o método 'get()':
# dict_1.get('key', default_value).

# Podemos verificar se uma determinada chave se encontra
# em um determinado dicionário:
print(f"'br' in countries? = {'br' in countries}")
print(f"'usa' in countries? = {'usa' in countries}")
print(f"'ru' in countries? = {'ru' in countries}")
print(f"'United States of America in countries? = "
	  f"{'United States of America 'in countries}")

print(15*'-')

if 'ru' in countries:
	russia = countries['ru']

print(" ")
print(25*'-')

# Podemos utilizar qualquer tipo de dado como chaves de dicionários:

# Dicionários misturando tipos:
print("Misturando dados em dicionários:")

# Tuplas por exemplo são bastante interessantes para serem usadas como
# chaves de dicionários em Python, pois as mesmas são imutáveis.
localidades = {
	(35.6895, 39.6917): 'Escritório em Tokio',
    (40.7128, 74.0060): 'Escritório em Nova Yoirk',
    (37.7749, 122.4194): 'Escritório em São Paulo',
}

print(f"localidades = {localidades} ")
print(15*'-')
print(f"type(localidades) = {type(localidades)}")
print(15*'-')

# Adicionando elementos em dicionários em Python:
print(f"Adicionando elementos em dicionários em Python:")
incomes = {'jan': 100, 'feb': 120, 'mar': 300}

print(f"incomes = {incomes}")
print(f"type(incomes) = {type(incomes)}")

print(15*'-')

# 1ª Forma de Adicionar Elementos em Um Dicionário:
# 1st Way to Add Elements to a Dictionary:
incomes['apr'] = 350
print("Including financial income for the month of April: ")
print("Incluindo a receita financeira do mês de abril: ")
print("incomes['apr'] = 350")
print(" ")
print(15*'-')
print(f"incomes = {incomes}")
print(15*'-')

print(" ")
print(25*'-')

# 2ª Forma de Adicionar Elementos em Um Dicionário:
# 2nd Way to Add Elements to a Dictionary:
new_income = {'may': 500}

# Com o método 'update()' tanto podemos fazer a inclusão de
# um novo objeto em um dicionário como atualizar o valor
# de um objeto já existene do mesmo.

incomes.update(new_income) # Mesmo efeito: incomes.update({'may': 500})

print("Including financial income for the month of May: ")
print("Incluindo a receita financeira do mês de maio: ")
print("new_income = {'may': 500}")
print("incomes.update(new_income)")
print(15*'-')
print(f"incomes = {incomes}")
print(15*'-')

print(" ")
print(25*'-')

# Atualizando dados em um dicionário:

# 1ª Forma - Usando atribuição:
# 1 st Way - Using attribution:

print(f"incomes BEFORE updating 'May': {incomes}")
incomes['may'] = 550
print("incomes['may'] = 550")
print(f"incomes AFTER updating 'May': {incomes}")
print(" ")
print(25*'-')
# 2ª Forma - Usando o método 'update()':
# 2nd Way - Using the update method:

print(f"incomes BEFORE updating 'May': {incomes}")
print("incomes.update({'may': 600})")
incomes.update({'may': 600})
print(f"incomes AFTER updating 'May': {incomes}")

print(" ")
print(25*'-')

# Conclusões:
# 1) A forma de incluir novos elementos ou de atualizar
# o valor de elementos de um dicionário é a mesma.
# 2) Em dicionários não podetemos ter chaves repetidas.

# Removendo elementos de um dicionário:
print("Removendo elementos de um dicionário:")
incomes = {'jan': 100, 'feb': 120, 'mar': 300}

# 1ª Foma - Usando o método 'pop()':
# 1st Way - Using the method 'pop()':
print("Using the method 'pop()':")
print()
print(f"Incomes BEFORE pop('mar'): {incomes} '")
ret = incomes.pop('mar') # ret = retorno
print(f"ret = incomes.pop('mar') = {ret}")

print(f"Incomes AFTER pop('mar'): {incomes} '")
# Observações:
# 1) Em dicionários, precisamos necessariamente
# informar uma chave que, se não for encontrada
# nele, será retorno um erro - KeyError.
# 2) Ao removermos um objeto de um dicionário
# usando o método 'pop(key)', o valor dele
# será sempre retornado.
print(" ")
print(25*"-")

# 2ª Foma - Usando o comando 'del()':
# 1st Way - Using the command 'del()':
print("Using the command 'del()':")
print("del incomes['feb']")

print(15*'_')
del incomes['feb']
print(f"incomes AFTER del incomes('feb') = {incomes}")
print(15*'_')

print(" ")
print(25*"-")

# Observação:
# 1) O comando del em Python é utilizado para deletar objetos,
# como variáveis, elementos de uma lista, elementos de um
# dicionário ou itens em sequências em geral. Ele não é restrito
# apenas para dicionários, embora você possa usá-lo para remover
# itens específicos de um dicionário.
# 2) Se tentarmos excluir um item de um dicionário usando uma chave
# que não existe no mesmo, iremos obter um erro - KeyError.
# 3) Usando o comando del, não ocorre o retorno de um valor.

# Importância do uso de dicionários:

# Imagine que vc tem um comércio eletrônico onde temos
# um carrinho de compras no qual adicionamos os
# seguintes produtos:

- Carrinho de compras:
product_1 =
	-name.product_1 ;
	-quantity.product_1 ;
	-price.product_1;
product_2 =
	-name.product_2;
	-quantity.product_2;
	-price.product_2;


# 1) Poderíamos usar uma lista para o carrinho de compras:
# shopping_cart = []
# product_1 = ['PlayStation 4', 1, 2300.00]
# product_2 = ['Good Of War', 1, 150.00]
#
# shopping_cart.append(product_1)
# shopping_cart.append(product_2)

# print(f"shopping_cart = {shopping_cart}")

# Dessa forma, teríamos que saber a qual índice está
# associado uma característica do produto.

# 2) Poderíamos utilizar uma tupla para esse problema? Sim
# shopping_cart = []
#
# product_1 = ('PlayStation 4', 1, 2300.00)
# product_2 = ('Good Of War', 1, 150.00)
#
# shopping_cart.append(product_1)
# shopping_cart.append(product_2)
#
# print(f"shopping_cart = {shopping_cart}")

# Dessa forma, também teríamos que saber a qual índice
# está associado uma característica do produto.

# 3) Poderíamos utilizar um dicionário para esse problema? Sim
shopping_cart = []

product_1 = {'name':'PlayStation 4', 'quantity': 1, 'price': 2300.00}
product_2 = {'name':'Good Of War', 'quantity': 1, 'price': 150.00}

shopping_cart.append(product_1)
shopping_cart.append(product_2)

print(f"shopping_cart = {shopping_cart}")

# Desta forma, facilmente adicionamos ou removemos produtos do
# carrinho de compra e, em cada um desses produtos, podemos ter
# certeza sobre cada informação.

print(" ")
print(25*'-')

d = dict(a=1, b=2, c=3)
print(f"dictionary d = {d}")
print(f"type(d) = {type(d)}")
print(15*"-")

# Zerando (limpando) um dicionário usando o método 'clear()':
print("Cleaning the dictionary 'd' using the method 'clear()':")
d.clear()
print(f"dictionary d AFTER clear() = {d}")

# Copiando um dicionário para outro:
d = dict(a=1, b=2, c=3)
print(f"dictionary d = {d}")
print(f"type(d) = {type(d)}")
print(15*"-")
# Forma 1 - Deep Copy - Usando o método 'copy()':

new_d = d.copy()

print(15*"-")
print(f"dictionary d = {d}")
print(f"dictionary new_d = {new_d}")
print(15*"-")
print("Adding a new element to the dictionary new_d:")
new_d.update({'d':4})
# ou new_d['d'] = 4
print(f"dictionary d = {d}")
print(f"dictionary new_d = {new_d}")
print(15*"-")

# Forma 2 - Shallow Copy - Usando atribuição:
new_d2 = d

print(15*"-")
print(f"dictionary d = {d}")
print(f"dictionary new_d2 = {new_d2}")
print(15*"-")

print("Adding a new element to the dictionary new_d:")
new_d2.update({'d':4})
# ou new_d2['d'] = 4
print(f"dictionary d = {d}")
print(f"dictionary new_d = {new_d2}")
print(15*"-")

"""
print("Dictionaries in Python:")

# Verificando se um dado objeto está em um dicionário:
print("Verificando se um dado objeto está em um dicionário:")
countries = {'br': 'Brazil',
			 'usa': 'United States of America',
			 'py': 'Paraguay'}

d = dict(a=1, b=2, c=3)
print(f"dictionary d = {d}")
print(f"type(d) = {type(d)}")
print(15*"-")

# Forma não usual de criação de dicionários:

other = {}.fromkeys('a', 'b')
print(f"other = {other}")
print(f"type(other) = {type(other)}")

print(" ")
print(25*'-')

user = {}.fromkeys(['name', 'points', 'email', 'profile'], 'unknown')
print(f"user = {user}")
print(f"type(user) = {type(user)}")

# O método 'fromkeys()' recebe dois parâmtreos: um iterável e um valor.
# Ele vai gerar para cada valor do iterável uma chave e irá atribuir a
# esta chave o valor informado.

print(" ")
print(25*'-')

veja = {}.fromkeys('test', 'value')
print(f"veja ={veja}")
print(f"type(veja) = {type(veja)}")

print(" ")
print(25*'-')

veja_2 = {}.fromkeys(range(1, 6), 'value')
print(f"veja_2 ={veja_2}")
print(f"type(veja_2) = {type(veja_2)}")