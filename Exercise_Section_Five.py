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

# --------------------------------------------------


print("Exercício - 13: ")

# Faça um algoritmo que calcule a média ponderada das notas de 3 provas.
# A primeira e a segunda prova têm peso 1 e a terceira tem peso 2. Ao
# final, mostrar a média do aluno e indicar se o aluno foi aprovado ou
# reprovado. A nota para aprovação deve ser igual ou superior a 60 pontos.

# def get_avarage(note1, note2, note3):
#
# 	return (note1 + note2 + 2*note3) / (4)
#
#
# def is_approved(avarage):
# 	if avarage >= 60:
# 		return "The student was aproved."
# 	else:
# 		return "The student wasn´t aproved."
#
#
# note_1 = float(input("Enter the first note: "))
# note_2 = float(input("Enter the second note: "))
# note_3 = float(input("Enter the third note: "))
#
# avarage = get_avarage(note_1, note_2, note_3)
# print(15*'-')
# print(f"avarage = {avarage}")
# print(15*'-')
# print(is_approved(avarage))
# print(15*'-')


# Outra forma:

def get_average(note1, note2, note3):
	'''Calculates the weighted average of three notes.'''
	# Verifica se as notas são números:
	if not all(isinstance(note, (int, float)) for note
			   in [note1, note2, note3]):
		raise TypeError("All notes must be numeric values.")

	return (note1 + note2 + 2 * note3) / 4


def is_approved(average):
	'''Checks if the student's average is above or equal to 60.'''
	# Verifica se a média é um número:
	if not isinstance(average, (int, float)):
		raise TypeError("Average must be a numeric value.")

	if average >= 60:
		return "The student was approved."
	else:
		return "The student wasn't approved."


try:
	note_1 = float(input("Enter the first note: "))
	note_2 = float(input("Enter the second note: "))
	note_3 = float(input("Enter the third note: "))

	average = get_average(note_1, note_2, note_3)
	print(15 * '-')
	print(f"Average = {average}")
	print(15 * '-')
	print(is_approved(average))
	print(15 * '-')
except ValueError:
	print("Please enter valid numerical values for the notes.")
except TypeError as e:
	print(f"Error: {e}")

print(25*'-')


# --------------------------------------------------


print("Exercício - 14: ")

# 14. A nota final de um estudante é calculada a partir de três notas
# atribuídas entre o intervalo de O até 10, respectivamente, a um
# trabalho de laboratório, a uma avaliação semestral e a um exame final.
# A média das três notas mencionadas anteriormente obedece aos pesos:
# Trabalho de Laboratório: 2; Avaliação Semestral: 3; Exame Final: 5. De
# acordo com o resultado, mostre na tela se o aluno está reprovado (média
# entre O e 2,9), de recuperação (entre 3 e 4,9) ou se foi aprovado. Faça
# todas as verificações necessárias.

def get_avarage(laboratory_work, sa_evaluation, final_exam):
	if not all(isinstance(note, (int, float)) for note in
			   [laboratory_work, sa_evaluation, final_exam]):
		raise TypeError(f"Please enter valid numerical values for "
						f"the notes.")
	if any(note < 0 or note > 10 for note in
		   [laboratory_work, sa_evaluation, final_exam]):
		raise ValueError("Grades must be values from 0 to 10!")

	return (2*laboratory_work + 3*sa_evaluation + 5*final_exam) / 10


def student_situation(avarage):
	if avarage >= 0 and avarage < 3.0:
		return "Failed student"
	elif avarage >= 3.0 and avarage < 5.0:
		return "Student in recovery"
	else:
		return "Student approved"

try:
	laboratory_work_1 = float(input("Enter your laboratory work score: "))
	sa_evaluation_1 = float(input("Enter your semester evaluation score: "))
	final_exam_1 = float(input("Enter your final exam scor: "))

	print("\n")
	avarage_1 = get_avarage(laboratory_work_1, sa_evaluation_1, final_exam_1)
	print(f"avarage_1 = {avarage_1}")
	print(15*'-')
	print(student_situation(avarage_1))
	print(15*'-')

except ValueError:
	print("Please enter a valid numerical value for all notes.")
except TypeError as err:
	print(f"An error ocorred: {err}")


print(25*'-')


# --------------------------------------------------

print("Exercício - 15: ")

# 15. Usando switch, escreva um programa que leia um inteiro entre
# 1 e 7 e imprima o dia da semana correspondente a este numero.
# Isto é, domingo se 1, segunda-feira se 2, e assim por diante.

def switch_case(option):
    switcher = {
    	"1": "Monday => segunda-feira",
		"2": "Tuesday => terça-feira",
		"3": "Wednesday => quarta-feira",
		"4": "Thursday => quinta-feira",
		"5": "Friday => sexta-feira",
		"6": "Saturday => sábado",
		"7": "Sunday => domingo"
    }

    return switcher.get(option, "Opção inválida")


day_of_the_week = input("Enter the chose option: ")
print(f"Chosen day of the week = {switch_case(day_of_the_week)}")

print(25*'-')

# --------------------------------------------------


print("Exercício - 16: ")

# 15. Usando switch, escreva um programa que leia um inteiro entre
# 1 e 7 e imprima o dia da semana correspondente a este numero.
# Isto é, domingo se 1, segunda-feira se 2, e assim por diante.

def switch_case(option):
    switcher = {
    	"1": "January => janeiro",
		"2": "February => fevereiro",
		"3": "March => março",
		"4": "April => abril",
		"5": "May => maio",
		"6": "June => junho",
		"7": "July => julho",
		"8": "August => agosto",
		"9": "September => setembro",
		"10": "October => outubro",
		"11": "November => novembro",
		"12": "Dezembro => dezembro"
    }

    return switcher.get(option, "Invalid option")


month = input("Enter the chose option for month: ")
print(f"Chosen day of the week = {switch_case(month)}")

print(25*'-')


# --------------------------------------------------------


print("Exercício - 17: ")

# 17. Faça um programa que calcule e mostre a área de um trapézio.
# Sabe - se que a área de um trapézio é dada por: A = (B + b)*h / 2,
# onde A = aréa do trabézio; B = base maior do trapézio; b = base
# menor do trapézio e h = altura do trapézio. Lembre-se a base maior e a
# base menor devem ser números maiores que zero.


def calculate_area_of_the_trapezoid(greater_base, minor_base, height):
	if not all(isinstance(measure, (int, float)) for measure in [greater_base, minor_base, height]):
		raise TypeError("Invalid type for trapezoid measures.")
	if any(measure <= 0 for measure in [greater_base, minor_base, height]):
		raise ValueError("Trapezoid measurements must be positive real numbers.")

	return ((greater_base + minor_base) * height) / 2.0


try:
	greater_base = float(input("Enter a value for greater_base: "))
	minor_base = float(input("Enter a value for minor_base: "))
	height = float(input("Enter a value for height: "))

	print("\nThe area of the trapezoid is:", calculate_area_of_the_trapezoid(greater_base, minor_base, height))

except (TypeError, ValueError) as err:
	print("Invalid input: ", err)


print(25*'-')

# # --------------------------------------------------------

print("Exercício - 18: ")

# 18. Faça um programa que mostre ao usuário um menu com 4 opções de
# operações matemáticas (as básicas, por exemplo). O usuário escolhe
# uma das opções e o seu programa então pede dois valores numéricos
# e realiza a operação, mostra o resultado e sai do mesmo.

print("Choose an option from those listed below: ")
print(15*'-')
print("1 - addition;")
print("2 - subtraction;")
print("3 - multiplication;")
print("4 - division;")
print(15*'-')
print(" ")

# option = int(input("Enter the option: "))
# first_value = float(input("Enter the first value: "))
# second_value = float(input("Enter the second value: "))

# 1ª Forma - sem o uso do 'while':
# if option == 1:
# 	result_1 = first_value + second_value
# 	print(f"{first_value} + {second_value} = {result_1}")
#
# elif option == 2:
# 	result_2 = first_value - second_value
# 	print(f"{first_value} - {second_value} = {result_2}")
#
# elif option == 3:
# 	result_3 = first_value * second_value
# 	print(f"{first_value} * {second_value} = {result_3}")
#
# elif option == 4:
# 	result_4 = first_value / second_value
# 	print(f"{first_value} / {second_value} = {result_4}")
#
# else:
# 	print("Invalid option")


# 2ª Forma - utilizando o while e funções:

def add(a, b):
	return a + b


def subtract(a, b):
	return a - b


def multiply(a, b):
	return a * b


def divide(a, b):
	if b != 0:
		return a / b
	else:
		return "Error: division by zero"


def show_menu():
	print("Choose an operation:")
	print("1. Addition")
	print("2. Subtraction")
	print("3. Multiplication")
	print("4. Division")
	print("Enter 'q' to quit")


def perform_operation(operation, a, b):
	if operation == '1':
		return add(a, b)
	elif operation == '2':
		return subtract(a, b)
	elif operation == '3':
		return multiply(a, b)
	elif operation == '4':
		return divide(a, b)
	else:
		return "Invalid option"


def main():
	while True:
		show_menu()
		choice = input("Enter your choice: ")
		if choice.lower() == 'q':
			break

		if choice not in ['1', '2', '3', '4']:
			print("Invalid option. Please try again.")
			continue

		num1 = float(input("Enter the first number: "))
		num2 = float(input("Enter the second number: "))

		result = perform_operation(choice, num1, num2)
		print(40 * '-')
		print("The result of the operation is:", result)
		print(40*'-')
		print(" ")


if __name__ == "__main__":
	main()

print(25*'-')

# --------------------------------------------


print("Exercício - 19: ")

# 19. Faça um programa para verificar se um determinado numero
# inteiro e divisivel por 3 ou 5, mas não simultaneamente pelos
# dois.


def is_divisible_by_3_or_5(number):
	if number % 3 == 0 or number % 5 == 0:
		return True
	else:
		return False


# chosen_number = int(input("Enter a number: "))
#
# if is_divisible_by_3_or_5(chosen_number):
# 	print(f"The number {chosen_number} IS divisible by 3 or 5.")
# else:
# 	print(f"The number {chosen_number} IS NOT divisible by 3 or 5.")


chosen_number = input("Enter a number or type 'q' to quit: ")

while chosen_number.lower() != 'q':
    if chosen_number.isdigit():  # Verifica se é um número
        if is_divisible_by_3_or_5(int(chosen_number)):
            print(f"The number {int(chosen_number)} IS divisible by 3 or 5.")
        else:
            print(f"The number {int(chosen_number)} IS NOT divisible by 3 or 5.")
    else:
        print("Invalid input. Please enter a number or 'q' to quit.")

    chosen_number = input("Enter a number or type 'q' to quit: ")

print(25*'-')


"""


print("Exercício - 20: ")

# 20. Dados três valores (A, B e C) verificar se eles podem ser valores
# dos lados de um triângulo e, se forem, se é um triângulo escaleno,
# equilatero ou isoscele, considerando os seguintes conceitos:
# - O comprimento de cada lado de um triângulo é menor do que a soma dos
# outros dois lados;
# - Chama se equilatero o triângulo que tem três lados iguais;
# -  Denominam se isosceles o triângulo que tem o comprimento de dois
# lados iguais;
# - Recebe o nome de escaleno o triângulo que tem os três lados
# diferentes.



print(25*'-')

