"""
Tipo Float (Real, Decimal):
- O separador das casas decimais na programação é o
ponto (.) e não a vírgula;

"""

# Errado:
# Observação: Errado do ponto de vista do tipo float, mas
# gera uma tupla

value = 1, 44
print(f"value: {value}")
print(f"type(value): {type(value)}")
print(" ")
print(25*"-")
# Certo do ponto de vista do float:
value = 1.44
print(f"value: {value}")
print(f"type(value): {type(value)}")
print(" ")
print(25*"-")

# Múltiplas atribuições:
print("Múltiplas Atribuções: ")

value1, value2 = 1, 44
print("value1, value2 = 1, 44")
print(f"value1 = {value1}")
print(f"type(value1): {type(value1)}")
print(f"value2 = {value2}")
print(f"type(value2): {type(value2)}")

print(" ")
print(25*"-")

# Todas as operações possíveis para um int também
# são possíveis para o tipo float
# Podemos converter um tipo float para um tipo int.
# Ao convertermos float para int, perdemos precisão.

result = int(value)
print(f"value = {value}")
print(f"result = int(value) =  {result}")
print(f"type(result) = {type(result)}")
print(" ")
print(25*"-")

# Podemos trabalhar com números complexos:
# number = 5j

number = complex(0, 5)
print(f"number = {number}")
print(f"number.real = {number.real}")
print(f"number.imag = {number.imag}")
print(f"number.abs = {number.__abs__()}")
print(f"Conjugado de number = {number.conjugate()}")

