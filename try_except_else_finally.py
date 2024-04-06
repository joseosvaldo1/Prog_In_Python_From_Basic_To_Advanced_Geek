"""
# Try, Except, Else and Fianlly:

- Dica de quando e onde tratar um código: TODA ENTRADA DE DADOS DEVE
SER TRATADA.

- A FUNÇÃO DO USUÁRIO É DESTRUIR O SEU SISTEMA.
# ----------------------------------------------------------

print("Exemplo_1:")

number = None

try:
	number = int(input("Enter a number: "))
except NameError:
	print("Undefined name!")
except ValueError:
	print("Incorrect value!")

print(f"You typed: {number}")


print("Exemplo_2:")

try:
	number = int(input("Enter a number: "))
except NameError:
	print("Undefined name!")
except ValueError:
	print("Incorrect value!")
else:
	print(f"You typed: {number}")

# Observações:
# 1) O bloco de código dentro else em um bloco try/except
# só será caso não ocorra no erro.
# 2) No Python, não é possível ter um bloco else para cada bloco except
# dentro de um bloco try/except. O bloco else em um bloco try/except é
# executado apenas se nenhum erro ocorrer dentro do bloco try. Ele não
# está vinculado a cada bloco except individualmente.


# ---------------------------------------------------------

print("Exemplo_3:")

try:
	number = int(input("Enter a number: "))
except NameError:
	print("Undefined name!")
except ValueError:
	print("Incorrect value!")
else:
	print(f"You typed: {number}")
finally:
	print("Executing the finally block.")

# Observações:
# 1) O bloco do 'finally' é SEMPRE executado independentemente
# se ocorreu ou erro/exceção ou não.
# 2) O bloco do 'finally' geralmente é utilizado para fechar ou
# para desalocar recursos.

# -----------------------------------------------------------
# Exemplo mais complexo - tratamento de erros INCORRETO:


def divide (a, b):
	return a / b

try:
	number_1 = float(input("Enter the first number: "))
except ValueError:
	print("The value must be numeric.")

try:
	number_2 = float(input("Enter the second number: "))
except ValueError:
	print("The value must be numeric.")

print(" ")

try:
	print(f"divide(number_1, number_2) = "
		  f"{divide(number_1, number_2) :.2f}")
except NameError:
	print("Incorrect Value!")
print(15*'-')

# -------------------------------------------------------
# Exemplo mais complexo - tratamento de erros CORRETO:
# Tratamento especídifco:

# Observação: você é responsável pelas entradas das suas funções.
# Então, trate as mesmas.


def divide(a, b):
	try:
		return float(a) / float(b)
	except ValueError:
		return "ValueError - The value must be numeric."
	except ZeroDivisionError:
		return "It is not possible to divide by zero."


number_1 = input("Enter the first number: ")
number_2 = input("Enter the second number: ")

print(f"divide(number_1, number_2) = "
	  f"{divide(number_1, number_2)}")

# ---------------------------------------------------------

# Exemplo mais complexo - tratamento de erros CORRETO:
# Tratamento genérico:

# Observação: você é responsável pelas entradas das suas funções.
# Então, trate as mesmas.


def divide(a, b):
	try:
		return float(a) / float(b)
	except:
		return "An unexpected error occurred."


number_1 = input("Enter the first number: ")
number_2 = input("Enter the second number: ")

print(f"divide(number_1, number_2) = "
	  f"{divide(number_1, number_2)}")

# ------------------------------------------------------


"""

# Exemplo mais complexo - tratamento de erros CORRETO:
# Tratamento semi-genérico:

# Observação: você é responsável pelas entradas das suas funções.
# Então, trate as mesmas.


def divide(a, b):
	try:
		return float(a) / float(b)
	except (ValueError, ZeroDivisionError) as err:
		return f"An unexpected error occurred: {err}"


number_1 = input("Enter the first number: ")
number_2 = input("Enter the second number: ")

print(f"divide(number_1, number_2) = "
	  f"{divide(number_1, number_2)}")









