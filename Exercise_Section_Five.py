"""
print("Exercício - 01: ")

# 1. Faça um programa que receba dois números e mostre
# qual deles e o maior:

input_text_1 = "Enter the first number: "
number1 = float(input(input_text_1))

input_text_2 = "Enter the second number: "
number2 = float(input(input_text_2))

print(" ")

if number1 > number2:
	print(f"The largest number is: {number1}.")
else:
	print(f"The largest number is: {number2}.")

print(25*'-')

import math

print("Exercício - 02: ")

# Leia um número fornecido pelo usuário. Se esse número for positivo,
# calcule a raiz quadrada do número. Se o numero for negativo, mostre
# uma mensagem dizendo que o numero e inválido.

number = float(input("Enter a number: "))

if number > 0.0:
	square_root_number = math.sqrt(number)
	print(f"The square root of the given number is: {square_root_number}")
else:
	print(f"Invalid number!")

print(25*'-')

import math

print("Exercício - 03: ")

# Leia um numero real. Se o numero for positivo, imprima a
# raiz quadrada. Do contrario, imprima o numero ao quadrado.

number = float(input("Enter a number: "))

if number > 0.0:
	square_root_number = math.sqrt(number)
	print(f"The square root of the given number "
		  f"is: {square_root_number}")
else:
	number_squared = number**2
	print(f"The square of the given number is: {number_squared}")

print(25*'-')

import math

print("Exercício - 04: ")

# Faça um programa que leia um número e, caso ele seja positivo,
# calcule e mostre:
# - O numero digitado ao quadrado
# - A raiz quadrada do numero digitado

number = float(input("Enter a number: "))

if number > 0.0:
	square_root_number = math.sqrt(number)
	number_squared = number ** 2

print(f"The square root of the given number is: {square_root_number:.2f}.")
print(f"The square of the given number is: {number_squared:.2f}.")

print(25*'-')

print("Exercício - 05: ")

# 5. Faça um programa que receba um numero inteiro e verifique se
# este numero e par ou impar.

number = float(input("Enter an integer number: "))

if number % 2 == 0:
	print("The given number is 'even (número par)'!")
else:
	print("The given number is 'odd (número ímpar)'!")

print(25*'-')

print("Exercício - 06: ")

# Escreva um programa que, dados dois números inteiros, mostre na
# tela o maior deles, assim como a diferença existente entre ambos.

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))


if number1 > number2:
	diference = number1 - number2
	print(f"The largest number is: {number1}")
	print(f"The diference between {number1} and {number2} "
		  f"is: {diference}")
else:
	diference = number2 - number1
	print(f"The largest number is: {number2}")
	print(f"The diference between {number2} and {number1} "
		  f"is: {diference}")

print(25*'-')


"""

print("Exercício - 07: ")



print(25*'-')
