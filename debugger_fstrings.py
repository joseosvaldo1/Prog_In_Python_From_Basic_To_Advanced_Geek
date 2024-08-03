"""
# Novos Recursos do Python:

- Debugger Mais Simples com f-strings:

# ---------------------------------------------------------------------


def multiply(number1: float, number2: float) -> float:
	return number1 * number2


result: float = multiply(4.2345, 6.7890)
print(f"The result is: {result:.4f}.")

print(15*'-')

print(f"The result is: {multiply(9, 4):.2f}")

print(15*'-')

print(f"{(value := 8 / 2)} is half of {value * 2}")

print(15*'-')


# ---------------------------------------------------------------------



"""


geek: str = 'Geek'

# Sem o uso de f-strings:
print(f"geek = '{geek}'")

print(15*'-')

# Usando f-strinds:
print(f"{geek = } ")

print(15*'-')

print(f"{geek.upper()[::-1] = } ")

print(15*'-')

