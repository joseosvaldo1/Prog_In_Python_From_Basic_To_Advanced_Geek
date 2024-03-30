"""
# List Comprehension - Parte II:

- Nós podemos adicionar estruturas condicionais lógicas as
nossas List Comprehension.

"""

# Exemplos:

# Exemplo_1:

numbers = [1, 2, 3, 4, 5, 6]
even_numbers_1 = [number for number in numbers if number % 2 == 0]
odd_numbers_1 = [number for number in numbers if number % 2 != 0]

print(f"numbers: {numbers}")
print(15*'-')
print(f"even_numbers_1: {even_numbers_1}")
print(15*'-')
print(f"odd_numbers_1: {odd_numbers_1}")
print(15*'-')
print(" ")
print(15*'-')

# Refatorando as listas de números pares e impares:

# Observação: Qualquer módulo de um número par por 2 é 0
# e o 0 em Python é 'False'.
even_numbers_2 = [number for number in numbers if not number % 2]

# Observação: Qualquer módulo de um número ímpar por 2 é 1
# e qualquer número diferente de 0 em Python é 'True'.
odd_numbers_2 = [number for number in numbers if number % 2]
print(f"even_numbers_2: {even_numbers_2}")
print(15*'-')
print(f"odd_numbers_2: {odd_numbers_2}")
print(15*'-')

# Exemplo_2:

result = [number*2 if number % 2 == 0 else number / 2 for number in numbers]
print(f"result: {result}")