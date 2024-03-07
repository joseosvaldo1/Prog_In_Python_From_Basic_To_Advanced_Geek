"""
# Entendendo o *args:

- O *args é um parâmetro de função como qualquer outro que você poderá
chamar de qualquer coisa, desde que comece com asterisco (*). Mas, por
convenção, utilizando *args para defini-lo.

* Mas o que é de fato o parâmetro *args?
- O parâmetro *args utilizado em uma função coloca os valores extras
informados na entrada em uma tupla. Então, desde já, lembre que tuplas
são imutáveis.

# -----------------------------------------------------------------------

def soma_todos_os_numeros(num1=0, num2=0, num3=0):
	return num1 + num2 + num3

print(soma_todos_os_numeros(4, 6, 9))
print(15*'-')
print(soma_todos_os_numeros(4, 6))
print(15*'-')
# print(soma_todos_os_numeros(4, 6, 9, 5)) # TypeError
# soma_todos_os_numeros() takes 3 positional arguments but 4 were given
print(15*'-')

# -----------------------------------------------------------------------

# # Entendendo o *args:
#
# # Refatorando a função soma_todo_os_numeros():
#
# def soma_todos_os_numeros(*args):
# 	return args
#
# print(soma_todos_os_numeros())
# print(soma_todos_os_numeros(1))
# print(soma_todos_os_numeros(2, 3))
# print(soma_todos_os_numeros(2, 3, 4))
# print(soma_todos_os_numeros(2, 3, 4, 5))

# Saída - Output:
# ()
# (1,)
# (2, 3)
# (2, 3, 4)
# (2, 3, 4, 5)

# print(15*'-')

# # Refatorando novamente a função soma_todo_os_numeros():
#
# def soma_todos_os_numeros(*args):
# 	total = 0
# 	for number in args:
# 		total += number
#
# 	return total
#
# print(soma_todos_os_numeros())  # => 0
# print(soma_todos_os_numeros(1)) # => 1
# print(soma_todos_os_numeros(2, 3)) # => 5
# print(soma_todos_os_numeros(2, 3, 4)) # => 9
# print(soma_todos_os_numeros(2, 3, 4, 5)) # => 14
#
# print(15*'-')
#
# # Refatorando novamente a função soma_todo_os_numeros():
#
# def soma_todos_os_numeros(*args):
# 	return sum(args)
#
# print(soma_todos_os_numeros())  # => 0
# print(soma_todos_os_numeros(1)) # => 1
# print(soma_todos_os_numeros(2, 3)) # => 5
# print(soma_todos_os_numeros(2, 3, 4)) # => 9
# print(soma_todos_os_numeros(2, 3, 4, 5)) # => 14
#
# print(15*'-')

# Refatorando novamente a função soma_todo_os_numeros():

def soma_todos_os_numeros(name, email, *args):
	return sum(args)

print(soma_todos_os_numeros('Angelina Jolie', 'aj@gmail.com'))  # => 0
print(soma_todos_os_numeros('Angelina Jolie', 'aj@gmail.com', 1)) # => 1
print(soma_todos_os_numeros('Angelina Jolie', 'aj@gmail.com', 2, 3)) # => 5
print(soma_todos_os_numeros('Angelina Jolie', 'aj@gmail.com', 2, 3, 4)) # => 9
print(soma_todos_os_numeros('Angelina Jolie', 'aj@gmail.com', 2, 3, 4, 5)) # => 14

print(15*'-')

# -----------------------------------------------------------------------

# Outro exemplo de utilização de *args:

def verifica_info(*args):
	if 'Geek' in args and 'University' in args:
		return "Bem vindo, Geek!"

	return "Eu não tenho certeza de quem você é!"

print(verifica_info())
print(15*'-')

print(verifica_info(1, True, 'University', 'Geek'))
print(15*'-')

print(verifica_info(1, 'University', 3.145))
print(15*'-')

# -----------------------------------------------------------------------

"""


def soma_todos_os_numeros(*args):
	return sum(args)


print(soma_todos_os_numeros())
print(15*'-')
print(soma_todos_os_numeros(3, 4, 5, 6))
print(15*'-')

numbers = [1, 2, 3, 4, 5, 6, 7]
numbers_2 = (1, 2, 3, 4, 5, 6, 7)
numbers_3 = {1, 2, 3, 4, 5, 6, 7}
# print(soma_todos_os_numeros(numbers))
# TypeError: unsupported operand type(s) for +: 'int' and 'list'

# Desempacotando os elementos da lista 'numbers':
num1, num2, num3, num4, num5, num6, num7 = numbers
print(soma_todos_os_numeros(num1, num2, num3, num4, num5, num6, num7))
print(15*'-')

# Desempacotando de forma automática com o *:
print(f"soma_todos_os_numeros(*numbers) - LIST = "
      f"{soma_todos_os_numeros(*numbers)}")
print(15*'-')
print(f"soma_todos_os_numeros(*numbers_2) - TUPLE = "
      f"{soma_todos_os_numeros(*numbers_2)}")
print(15*'-')
print(f"soma_todos_os_numeros(*numbers_2) - SET = "
      f"{soma_todos_os_numeros(*numbers_3)}")
print(15*'-')

# Observação: o * serve para que informemos ao Python estamos
# passando como argumento para a função uma coleação de dados.
# Dessa forma, ele saberá que precisará desempacotar esses dados.



