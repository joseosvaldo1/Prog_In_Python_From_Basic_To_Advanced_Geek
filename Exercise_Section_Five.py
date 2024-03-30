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

print("Exercício - 07: ")

# Faça um programa que receba dois numeros e mostre o maior Se por
# acaso, os dois numeros forem iguais, imprima a mensagem Números
# iguais

def choose_the_biggest_number(number1, number2):
	if number1 > number2:
		return number1
	elif number1 == number2:
		return "Números iguais"
	else:
		return number2

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number "))

print(" ")
print("The biggest number is: " +
	  str(choose_the_biggest_number(num1, num2)))



print(25*'-')

print("Exercício - 08: ")

# Faça um programa que leia 2 notas de um aluno, verifique se as notas
# são válidas e exiba na tela a media destas notas. Uma nota valida deve
# ser, obrigatoriamente, um valor entre 00 e 100, onde caso a nota não
# possua um valor válido, este fato deve ser informado ao usuario e o
# programa termina.

grade1 = float(input("Enter the first grade: "))
grade2 = float(input("Enter the second grade: "))

if ((grade1 >= 00 and grade1 <= 100) and (grade2 >= 00 and grade2 <= 100)):
	avarage = (grade1 + grade2) / 2.0
	print("The average grade is: " + str(avarage))
else:
	print("One of the grades entered is invalid!")

print(25*'-')

print("Exercício - 09: ")

# Leia o salário de um trabalhador e o valor da prestação de um
# empréstimo. Se a prestação for maior que 20% do salário, imprima
# Empréstimo não concedido; caso contrario, imprima Empréstimo
# concedido

salary = float(input("Enter the value of the worker's salary: "))
installment = float(input("Enter the installment value: "))

loan_granting_criteria = 0.20*salary

if installment > loan_granting_criteria:
	print("Empréstimo não concedido")
else:
	print("Empréstimo concedido")

print(25*'-')

print("Exercício - 10: ")

# Faça um programa que receba a altura e o sexo de uma pessoa e calcule
# e mostre seu peso ileal, utilizando as seguintes formulas (onde h
# corresponde a altura)
#  * Homens (72.7*h) - 58
#  * Mulheres (62.1*h) - 44.7

gender = input("Enter your gender - M/F: ")
height = float(input("Enter a value for height in meters: "))


if gender == "M":
	ideal_weight = 72.7*height - 58.0
else:
	ideal_weight = 62.1 * height - 44.7

print(f"Your ideal weight is: {ideal_weight:.2f} ")

print(25*'-')

print("Exercício - 11: ")

# Escreva um programa que leia um número inteiro maior do que zero e
# devolva, na tela, a soma de todos os seus algarismos. Por exemplo,
# ao número 251 corresponderá o valor 8(2+5+ 1). Se o número lido não
# for maior do que zero, o programa terminará com a mensagem
# “Número inválido”.

number = input("Enter a integer number: ")

# Usando um laço for:

# digits = []
#
# for char in number:
# 	digit = int(char)
# 	digits.append(digit)
#
# print(f"digits = {digits}")
# print(f"The digits of the number are: {sum(digits)}")

# Usando List Comprehension:
digits = [int(char) for char in number]
print(f"list_of_digits = {digits}")
print(f"sum of digits = {sum(digits)}")

print(25*'-')

from math import log

print("Exercício - 12: ")

# Ler um número inteiro. Se o número lido for negativo, escreva a
# mensagem “Número inválido”. Se o número for positivo, calcular o
# logaritmo deste numero.

number = float(input("Enter a number: "))

if number < 0:
	print("Número inválido")
else:
	print(f"The decimal logarithm of the given number is:  "
		  f"{log(number, 10)}")

print(25*'-')


"""


print("Exercício - 13: ")

# Faça um algoritmo que calcule a média ponderada das notas de 3 provas.
# A primeira e a segunda prova têm peso 1 e a terceira tem peso 2. Ao
# final, mostrar a média do aluno e indicar se o aluno foi aprovado ou
# reprovado. A nota para aprovação deve ser igual ou superior a 60 pontos.



print(25*'-')


