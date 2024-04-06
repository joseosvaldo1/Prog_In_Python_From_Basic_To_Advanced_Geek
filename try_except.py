"""
# O Bloco Try/Except:

- Utilizamos o bloco 'try/except' para tratar erros que podem
ocorrer no nosso código, prevenindo assim que o programa pare
de funcionar e o usuário receba mensagens de erro inesperadas.

- A forma geral mais simples do bloco try/except é:

try:
	<Execução problemática>
except:
	<O que deve ser feito em caso de problemas.>

# Exemplo_1 - tratando um erro genérico:

# geek()  # => NameError: name 'geek' is not defined

print("Exemplo_1:")
try:
	geek()
except:
	print('Ocorreu um erro')

print(15*'-')

# Explicação do funcionamento: Foi informado o seguinte no código: "Tente
# executar a função 'geek()'. Caso encontre/capture um erro/exceção,
# imprima a mensagem "Ocorreu um erro".

# Observação: A estrutura try/except pode capturar qualquer tipo de erro.


# ---------------------------------------------------------

# Exemplo_2 - tratando um erro genérico:

print("Exemplo_2:")

# len(5)  # => TypeError: object of type 'int' has no len()

try:
	len(5)
except:
	print('Ocorreu um erro')

print(15*'-')

# Observação: Tratar erro de forma genérica não é a melhor forma de
tratamento de erro. O ideal é SEMPRE tratar o erro de forma específica.

# ----------------------------------------------------

# Exemplo_3 - tratando um erro específico:

print("Exemplo_2:")

try:
	geek()
except NameError:
	print("You are using a non-existent function.")

# Exemplo_4 - tratando um erro específico:

print("Exemplo_4:")

try:
	len(5)
except TypeError:
	print("It is not possible to use this data type")

# Exemplo_5 - tratando um erro específico - com detalhes do erro:

print("Exemplo_5:")

try:
	len(5)
except TypeError as err:
	print(f"The application generated the following error: '{err}'. ")

# Exemplo_6 - tratando erros específicos com o tratamento genérico.

print("Exemplo_6:")
try:
	geek()  # => NameError
	# len(5) # => TypeError
	# print("Geek"[9])  # => IndexError
except NameError as err_a:
	print(f"A NameError occurred: '{err_a}'")
except TypeError as err_b:
	print(f"A TypeError occurred: '{err_b}'")
except:
	print(f"An Unexpected error occurred.")


# Observação: Podemos efetuar diversos tratamentos de erros
# de uma única vez.

"""

# Exemplo_7:
print("Exemplo_7:")

def get_value(dictionary, key):
	try:
		return dictionary[key]
	except KeyError:
		return None
	except TypeError:
		return None


dic = {'name': 'Geek'}
print(f"get_value(dic, 'name') = {get_value(dic, 'name')}")
print(f"get_value(dic, 'game') = {get_value(dic, 'game')}")
print(f"get_value(dic, 'game') = {get_value(dic, 7)}")


