"""
# Entendendo o **kwargs:

- Poderíamos chamar esse parâmetro como **x; mas, por convenção,
chamamos de **kwargs.

- Este é só mais um parâmetro, mas diferente do *args que coloca os
valores extras em uma tupla, o **kwargs exige que utilizemos parâmetros
nomeados e transforma esses parâmetros extras em um dicionário.


# def cores_favoritas(**kwargs):
# 	print(kwargs)


# 'Cores Favoritas: '
#
# cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco'))
#
# print(15*'-')

def cores_favoritas(**kwargs):
	for person, color in kwargs.items():
		print(f"A cor favorita de {person.title()} é: {color} ")


cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

print(15*'-')

# Observação: Os parâmetros *args e **kwargs não são obrigatórios.
cores_favoritas()
print(15*'-')
cores_favoritas(geek='navy')
print(15*'-')

# Um exemplo mais complexo envolvendo **kwargs:

def cumprimento_especial(**kwargs):
	if 'geek' in kwargs and kwargs['geek'] == 'Python':
		return "Você recebeu um cumprimento Pythônico Geek!"
	elif 'geek' in kwargs:
		return f"{kwargs['geek']} Geek!"
	return "Não tenho certeza de quem você é!"


print(15*'-')
print(cumprimento_especial())
print(15*'-')
print(cumprimento_especial(geek='Python'))
print(15*'-')
print(cumprimento_especial(geek='Oi'))
print(15*'-')
print(cumprimento_especial(geek='especial!'))
print(15*'-')

# Nas nossas funções, podemos ter (NESTA ORDEM):
# 1º) - Parâmetros obrigatórios;
# 2º) - *args;
# 3º) - Parâmetros default - padrões (não obrigatórios);
# 4º) - **kwargs.

def my_function(age, name, *args, single=False, **kwargs):
	print(f"{name} is {age} years-old")

	print(args)

	if single is True:
		print('Single')
	else:
		print("Married")

	print(kwargs)

my_function(8, 'Julia')
print(15*'-')
my_function(18, 'Felicity', 4, 5, 3, single=True)
print(15*'-')
my_function(34, 'Felipe', me='Don´t', you='Go!')
print(15*'-')
my_function(19, 'Carla', 9, 4, 3, java=False, python=True)


# Entenda por que é importante manter a ordem dos parâmetros
# nas declarações de funções em Python:

# Função com a ordem correta dos parâmetros:
def show_info(a, b, *args, instructor='Geek', **kwargs):
	return [a, b, args, instructor, kwargs]

# print(show_info(1, 2,3,
# 				  sobrenome='University',
# 				  cargo='Instrutor'))

# Saída: [1, 2, (3,), 'Geek', {'sobrenome': 'University',
# 'cargo': 'Instrutor'}]

# ---------------------------------------------------------

# Função com a ordem incorreta dos parâmetros:
# def show_info(a, b, instructor='Geek', *args,  **kwargs):
# 	return [a, b, args, instructor, kwargs]
#
# print(show_info(1, 2,3,
#                 sobrenome='University',
# 	              cargo='Instrutor'))
#
# Saída: [1, 2, (), 3, {'sobrenome': 'University', 'cargo': 'Instrutor'}]

# ---------------------------------------------------------

print(show_info(1, 2,3,
				sobrenome='University',
				cargo='Instrutor'))

# Esperamos obter pela ordem:
# a = 1
# b = 2
# args = (3,)
# instructor = 'Geek'
# kwargs = {'sobrenome': 'University', 'cargo': 'Instrutor' }


# Desempacotando dados com **kwargs:

def show_names(**kwargs):
	return f"{kwargs['name']} {kwargs['surname']}"


names = {'name': 'Falicity', 'surname': 'Jones'}

# print(show_names(names)) # => TypeError
# TypeError: show_names() takes 0 positional arguments
# but 1 was given

print(f"show_names(name='Falicity', surname='Jones') = "
	  f"{show_names(name='Falicity', surname='Jones')}")
print(15*'-')
print(f"show_names(**names) = {show_names(**names)} ")
print(15*'-')

"""

# Outro Exemplo:

def sum_multiple_numbers(a, b, c, **kwargs):
	print(a+b+c)

list_numbers = [1, 2, 3]
tuple_numbers = (1, 2, 3)
set_numbers = {1, 2, 3}
dict_numbers = dict(a=1, b=2, c=3, name='Geek')

print(f"list_numbers = {list_numbers}")
print("sum - list_numbers:", end=' ')
sum_multiple_numbers(*list_numbers)
print(15*'-')


print(f"tuple_numbers = {tuple_numbers}")
print("sum - tuple_numbers:", end=' ')
sum_multiple_numbers(*tuple_numbers)
print(15*'-')

print(f"set_numbers = {set_numbers}")
print("sum - set_numbers:", end=' ')
sum_multiple_numbers(*set_numbers)
print(15*'-')

print(f"dict_numbers = {dict_numbers}")
print("sum - set_numbers:", end=' ')
sum_multiple_numbers(**dict_numbers, lang='Pyhton')
print(15*'-')


# Observação: Os nomes das chaves em um dicionário devem ser os mesmos
# dos parâmetros da função.

# dict_numbers_2 = dict(d=1, e=2, f=3)
# print(f"dict_numbers = {dict_numbers_2}")
# print("sum - set_numbers_2:", end=' ')
# sum_multiple_numbers(**dict_numbers_2) # => TyperError
# TypeError: sum_multiple_numbers() got an unexpected
# keyword argument 'd'
# As chaves são 'd', 'e' e 'f' enquanto os parâmetros da função
# são 'a', 'b' e 'c' - o que gera o TypeError.
# print(15*'-')

