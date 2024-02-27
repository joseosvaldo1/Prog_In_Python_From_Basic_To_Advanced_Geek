"""
Exercises Section Four - Geek:
print("Exercise 1:")
integer_number = int(input("Type an integer number: "))
print(f"The integer number is: '{integer_number}'")

print(25*'-')
print("Exercise 2:")
real_number = float(input("Type a real number: "))
print(f"The real number is: '{real_number}'")
print(25*'-')

print("Exercise 3:")
number1 = int(input("Type the first number: "))
number2 = int(input("Type the second number: "))
number3 = int(input("Type the third number: "))
print(" ")
sum = number1 + number2 + number3
print(f"The sum of three numbers is: '{sum}'!")
print(25*'-')

print("Exercise 4:")
real_number = float(input("Type a real number: "))
print(f"The square number written is: {real_number**2} ")

print(25*'-')

print("Exercise 5: ")
real_number = float(input("Type a real number: "))
print(f"The fifth part of the given number " +
      f"is: {real_number/5} ")

print(25*'-')

print("Exercise 6: ")
question = "Enter the temperature in Celsius: "
temperature_in_celsius= float(input(question))
temperature_in_farenheit = (temperature_in_celsius)*(9.0/5.0) + 32.0

print(f"The temperature in Farenheit is: '{temperature_in_farenheit} ºF'")

print(25*'-')

print("Exercise 7: ")
question = "Enter the temperature in Farenheit: "
temperature_in_farenheit= float(input(question))
temperature_in_celsius = (5.0*(temperature_in_farenheit - 32.0))/9.0

print(f"The temperature in Farenheit is: "
      f"'{temperature_in_celsius} ºC'")

print(25*'-')

print("Exercise 7: ")
question = "Enter the temperature in Farenheit: "
temperature_in_farenheit= float(input(question))
temperature_in_celsius = (5.0*(temperature_in_farenheit - 32.0))/9.0

print(f"The temperature in Farenheit is: "
      f"'{temperature_in_celsius} ºC'")

print(25*'-')

print("Exercise 8: ")
text= "Enter the temperature in Kelvin: "
temperature_in_kelvin= float(input(text))
temperature_in_celsius = temperature_in_kelvin - 273.15

print(f"The temperature in Celsius is: "
      f"'{temperature_in_celsius:.2f} ºC'")

print(25*'-')

print("Exercise 9: ")
text= "Enter the temperature in Celsius: "
temperature_in_celsius= float(input(text))
temperature_in_kelvin= temperature_in_celsius + 273.15

print(f"The temperature in Celsius is: "
      f"'{temperature_in_kelvin:.2f} K'")

print(25*'-')

print("Exercise 10: ")
text= "Enter a speed in km/h: "
speed_in_km_per_h = float(input(text))
speed_in_m_per_s = speed_in_km_per_h / 3.6
print(f"The speed in m/s is: "
      f"'{speed_in_m_per_s:.2f} m/s'")

print(25*'-')

print("Exercise 11: ")
text= "Enter a speed in m/s: "

speed_in_m_per_s = float(input(text))
speed_in_km_per_h= speed_in_m_per_s * 3.6

print(f"The speed in m/s is: "
      f"'{speed_in_km_per_h:.2f} km/h'")

print(25*'-')

print("Exercise 12: ")
text= "Enter a distance in miles: "

distance_in_miles = float(input(text))
distance_in_km = 1.61*distance_in_miles

print(f"The distance given in quilemeter is: " +
      f"'{distance_in_km:.2f}'")

print(25*'-')

print("Exercise 13: ")
text= "Enter a distance in quilometers: "

distance_in_quilometers = float(input(text))
distance_in_miles = distance_in_quilometers/1.61

print(f"The distance given in quilometers is: " +
      f"'{distance_in_miles:.2f}'")

print(25*'-')

# import math

print("Exercise 14: ")
text = "Enter an angle in degrees: "
angle_in_degrees = float(input(text))
angle_in_radians = (angle_in_degrees*math.pi)/180

print(f"The angle in radians is: "
      f"'{angle_in_radians:.2f} rad'")

print(25*'-')

# import math

print("Exercise 15: ")
text = "Enter an angle in radians: "
angle_in_radians = float(input(text))
angle_in_degrees = (angle_in_radians*180)/(math.pi)

print(f"The angle in degrees is: "
      f"'{angle_in_degrees:.2f}º'")

print(25*'-')

print("Exercise 16: ")
input_text = "Enter a measurement value in inches: "
measurement_in_inches = float(input(input_text))
measurement_in_cm = measurement_in_inches*2.54

print(f"The measurement in centimeters is: "
      f"'{measurement_in_cm:.2f} cm.'")

print(25*'-')

print("Exercise 17: ")
input_text = "Enter a measurement value in centimeters: "
measurement_in_cm= float(input(input_text))
measurement_in_inches = measurement_in_cm/2.54

print(f"The measurement in inches is: "
      f"'{measurement_in_inches:.2f} inches.'")

print(25*'-')

print("Exercise 18: ")
input_text = "Enter a volume value in cubic meters: "
volume_in_cubic_meters= float(input(input_text))
volume_in_liters = 1000*volume_in_cubic_meters

print(f"The volume value in liters is: "
      f"'{volume_in_liters:.2f} liters.'")

print(25*'-')

print("Exercise 19: ")
input_text = "Enter a volume value in 'liters': "
volume_in_liters = float(input(input_text))
volume_in_cubic_meters = volume_in_liters/1000.00

print(f"The volume value in 'cubic meters' is: "
      f"'{volume_in_cubic_meters:.2f} cubic meters.'")

print(25*'-')

print("Exercise 20: ")
input_text = "Enter a mass value in 'kg': "
mass_in_kg = float(input(input_text))
mass_in_pounds = (mass_in_kg)/0.45

print(f"The value in 'pounds' for value given is: "
      f"'{mass_in_pounds:.2f} pounds.'")

print(25*'-')

print("Exercise 21: ")
input_text = "Enter a mass value in 'pounds': "
mass_in_pounds = float(input(input_text))
mass_in_kg = (mass_in_pounds)*0.45

print(f"The value in 'kg for value given is: "
      f"'{mass_in_kg:.2f} Kg'")

print(25*'-')

print("Exercise 22: ")
input_text = "Enter a length value in yards: "
length_in_yard = float(input(input_text))
length_in_meters = 0.91*length_in_yard

print(f"The length in meters is: '{length_in_meters:.2f} m,'")

print(25*'-')

print("Exercise 23: ")
input_text = "Enter a length value in meters: "
length_in_meters = float(input(input_text))
length_in_yards = 0.91/length_in_meters

print(f"The length in yards is: '{length_in_yards:.2f} yards,'")

print(25*'-')

print("Exercise 24: ")
input_text = "Enter an area value in square meters: "
area_in_sqr_meters = float(input(input_text))
area_in_acre = 0.000247 * area_in_sqr_meters

print(f"The area in acre is: '{area_in_acre:.2f} acre.'")

print(25*'-')

print("Exercise 25: ")
input_text = "Enter an area value in acre: "
area_in_acre = float(input(input_text))
area_in_sqr_meters = 4048.58*area_in_acre

print(f"The area in square meter is: '{area_in_sqr_meters:.2f} m².'")

print(25*'-')

print("Exercise 26: ")
input_text = "Enter an area value in square meters: "
area_in_sqr_meters = float(input(input_text))
area_in_ha = 0.0001*area_in_sqr_meters

print(f"The area in ha is: '{area_in_ha:.2f} ha.'")

print(25*'-')

print("Exercise 27: ")
input_text = "Enter an area value in square meters: "
area_in_ha = float(input(input_text))
area_in_sqr_meters = 10000*area_in_ha

print(f"The area in m² is: '{area_in_sqr_meters:.2f} m².'")

print(25*'-')

print("Exercise 28: ")
value_1 = float(input("Enter a first value: "))
value_2 = float(input("Enter a second value: "))
value_3 = float(input("Enter a third value: "))
print(" ")
sum_of_square_of_value = value_1**2 + value_2**2 + value_3**2

print(f"The sum of square values is: '{sum_of_square_of_value}")

print(25*'-')


print("Exercise 29: ")
test_score_1 = float(input("Enter a first test score: "))
test_score_2 = float(input("Enter a second test score: "))
test_score_3 = float(input("Enter a third test score: "))
test_score_4 = float(input("Enter a fourth test score: "))
print(" ")
sum = test_score_1 + test_score_2 + test_score_3 + test_score_4
avarage = sum / 4.0

print(f"The avarage of four test scores is: '{avarage:.2f}'")

print(25*'-')

print("Exercise 30: ")
text_input = "Enter a monetary value in reais: R$ "
amount_in_real = float(input(text_input))
dollar_exchange_rate = 4.95 # EM 29/01/2024
amount_in_dollars = amount_in_real*dollar_exchange_rate

print(f"The amount in dollars is: '{amount_in_dollars:.2f}'")
print(25*'-')

print("Exercise 31: ")
text_input = "Enter an integer value: "
number = int(input(text_input))

predecesser_number = number - 1
successor_number = number + 1

print(f"The predecessor of '{number}' is: '{predecesser_number}'.")
print(f"The successor of '{number}' is: '{successor_number}'.")
print(25*'-')

print("Exercise 32: ")
text_input = "Enter an integer value: "
number = int(input(text_input))

predecesser_number_doble = 2*number - 1
successor_number_triple = 3*number + 1

result = predecesser_number_doble + successor_number_triple

print(f"result = '{result}.'")

print(25*'-')

print("Exercise 33: ")
text_input = "Enter a side value for the square: "
side_value = float(input(text_input))

square_area = side_value ** 2

print(f"The area of the square of {side_value} side is: '{square_area}.'")
print(25*'-')

# import math
print("Exercise 34: ")
text_input = "Type a value for the radius of the circle: "
radius_value = float(input(text_input))

circle_area = math.pi * (radius_value ** 2)

print(f"The area of the circle of {radius_value} "
      f"radius is: '{circle_area:.2f}.'")
print(25*'-')

# import math

print("Exercise 34: ")
text_input_1 = "Enter a measure value for the first leg: "
first_leg = float(input(text_input_1))
text_input_2 = "Enter a measure value for the second leg: "
second_leg = float(input(text_input_2))

hypotenuse = math.sqrt(first_leg**2 + second_leg**2)

print(f"The hypotenuse value is: {hypotenuse:.2f} ")

print(25*'-')

import math

print("Exercise 36: ")
text_input_1 = "Enter a measure value for the height:  "
height= float(input(text_input_1))
text_input_2 = "Enter a measure value for the redius: "
radius= float(input(text_input_2))

cylinder_volume = math.pi * (radius**2) * (height)


print(f"The cylinder volume is: {cylinder_volume:.2f}.")

print(25*'-')

print("Exercise 37: ")
text_input_1 = "Enter product price without discount: "
price = float(input(text_input_1))

text_input_2 = "Enter the discount rate: "
discount_rate = float(input(text_input_2))

price_with_discount = (1-discount_rate/100)*price

print(f"The price with {discount_rate:.2f} % of "
      f"discount is: R$ {price_with_discount:.2f}")

print(25*'-')

print("Exercise 38: ")
text_input_1 = "Enter an amount for the employee's salary: "
salary = float(input(text_input_1))

text_input_2 = "Enter a salary increase percentage: "
percentage_increase = float(input(text_input_2))

new_salary = (1 + percentage_increase/100)*salary

print(f"The new salary is: 'R$ {new_salary:.2f}'.")

print(25*'-')

print("Exercise 39: ")
text_input = "Enter the value of the prize to be shared: R$ "
total_prize = float(input(text_input))

first_prize = total_prize*0.46
second_prize = total_prize*0.32
third_prize = total_prize*0.22

print(f"The first winner received: R$ {first_prize:.2f}.")
print(f"The second winner received: R$ {second_prize:.2f}.")
print(f"The third winner received: R$ {third_prize:.2f}.")

print(25*'-')

print("Exercise 40: ")
text_input = "Enter the number of days worked for the plumber: "

number_of_days_worked = int(input(text_input))
salary_plumber = (1 - 0.08)*(number_of_days_worked*30.00)

print(f"The salary of the plumber is: "
	  f"R$ {salary_plumber:.2f}.")
print(25*'-')

print("Exercise 41: ")
text_input_1 = "Enter the hourly rate: R$ "
text_input_2 = "Enter the number of hours worked: "

hourly_rate = float(input(text_input_1))
hours_worked = float(input(text_input_2))
additional = 0.10 # Adicional de 10%

salary = (1 + additional)*hourly_rate*hours_worked

print(f"The salary of employee is: R$ {salary:.2f}.")

print(25*'-')

print("Exercise 42: ")

# Solicita ao usuário que insira o salário-base
# do funcionário:
base_salary = float(input("Enter the employee's "
						  "base salary: "))

# Solicita ao usuário que insira o valor adicional
# (gratificação):
additional = float(input("Enter the additional "
						 "amount on top of the "
						 "base salary (in decimal "
						 "form, e.g., 0.05 for 5%): "))

# Solicita ao usuário que insira a taxa de imposto
# de renda:
tax_rate = float(input("Enter the income tax rate "
					   "that will be levied on the "
					   "base salary (in decimal form, "
					   "e.g., 0.07 for 7%): "))

# Calcula o salário a receber com base nos
# nos dados de entrada fornecidos:
salary_to_be_received = (1 + additional - tax_rate) * base_salary

# Imprime o resultado
print(f"The salary to be received will be: R$ "
	  f"{salary_to_be_received:.2f}")


print(25*'-')

print("Exercise 43: ")

input_text_1 = " Enter the total value of the customer's purchases: R$ "
total_value_purchase = float(input(input_text_1))

total_payable_discount = (0.90)*total_value_purchase
installment_amount = total_value_purchase / 3.0
seller_commission_amount_3 = 0.05*total_payable_discount
seller_commission_amount_4 = 0.05*total_value_purchase

print(15*'-')

print("Options:")
print("Enter '1' for: 'Total payable with ten percent discount'")
print(f"Enter '2' for: 'Value of each installment, in 3 "
	  f"interest-free installments")
print(f"Enter '3' for: 'The seller's commission, if the sale "
	  f"is cash - 5% of the discounted value")
print(f"Enter '4' for: 'the seller's commission, if the sale "
	  f"is made - in installments - 5% of the total value")
print(f"Enter '5' do exit:")

print(15*'-')

input_text_2 = "Enter the option: "
option = int(input(input_text_2))

while option != 5:

	if option == 1:

		print(15*'-')
		print(f"The total payable with ten percent "
			  f"of discount is: R$ {total_payable_discount:.2f}.")
		print(15 * '-')
		print(" ")

	elif option == 2:

		print(15*'-')
		print(f"The installment value is: "
			  f"R$ {installment_amount:.2f}. ")
		print(15 * '-')
		print(" ")

	elif option == 3:

		print(15*'-')
		print(f"The seller's commission, if the sale is cash - " +
			  f"5% of the discounted value: R${seller_commission_amount_3:.2f}")
		print(15 * '-')
		print(" ")

	elif option == 4:

		print(15*'-')
		print(f"The seller's commission, if the sale is made in installments - " +
			  f"5% of the total value: R$ {seller_commission_amount_4:.2f}.")
		print(15 * '-')
		print(" ")

	else:

		print(15*'-')
		print("Invalid option. Enter a valid option (from 1 to 5) please!")
		print(15 * '-')
		print(" ")

	input_text_2 = "Enter the option: "
	option = int(input(input_text_2))


print(25*'-')

print("Exercise 44: ")

# Receba a altura do degrau de uma escada e a altura que o
# usuário deseja alcançar subindo a escada. Calcule e mostre
# quantos degraus o usuário deverá subir para atingir seu
# objetivo.

input_text_1 = "Enter the height of the step in centimeters: "
input_text_2 = "Enter the desired height to reach in centimeters: "

step_height = float(input(input_text_1))
desired_height = float(input(input_text_2))

step_quantity = int(desired_height / step_height)

print(f"The quantity of steps is: {step_quantity} steps")

print(25*'-')

print("Exercise 45: ")

# Faça um programa para converter uma letra maiúscula em letra
# minúscula. Use a tabela ASCII para resolver o problema.

# Get an uppercase letter from the user
uppercase_letter = input("Enter an uppercase letter: ")

# Convert the uppercase letter to lowercase using ASCII table:
ascii_value_uppercase = ord(uppercase_letter)
ascii_value_lowercase = ascii_value_uppercase + 32

# The difference between uppercase and lowercase is 32 in the ASCII table
lowercase_letter = chr(ascii_value_lowercase)

# Display the result:
print(f"The corresponding lowercase letter is: {lowercase_letter}")

print(25*'-')

print("Exercise 46: ")
# Faça um programa que leia um número inteiro positivo de três dígitos
# (de 100 a 999). Gere outro número formado pelos dígitos invertidos do
# número lido. Exemplo:
#			Número Lido:   123
#			Número Gerado: 321

input_text = "Enter a number between 100 and 999: "
read_number = input(input_text)

generated_number_array = list(read_number)
generated_number = ''.join(generated_number_array[::-1])

print(f"The generated number is: {generated_number}")

print(25*'-')

print("Exercise 47: ")
# Leia um número inteiro de 4 dígitos (de 1000 a 9999) e
# imprima 1 dígito por linha.

input_text = "Enter an integer from 1000 to 9999: "

read_number = input(input_text)

# Convertendo em uma lista:
read_number_list = list(read_number)

for digit in read_number_list:
	print(digit)


print(25*'-')

print("Exercise 48: ")
# Leia um valor inteiro em segundos, e
# imprima-o em horas, minutos e segundos.

input_text = "Enter a time interval in seconds: "

time_in_seconds = int(input(input_text))

hours = int(time_in_seconds / 3600)
minutes = int((time_in_seconds % 3600) / 60)
seconds = int(time_in_seconds % 60)

print(f"{hours} h: {minutes} min: {seconds} s")

print(25*'-')

print("Exercise 49: ")

# Faça um programa para leia o horário (hora, minuto e segundo) de
# início e a duração, em segundos, de uma experiência biológica. O
# programa deve resultar com o novo horário (hora, minuto e segundo)
# do termino da mesma.


# Function to calculate the new time based on the start time
# and duration in seconds:
def calculate_end_time(start_hour, start_minute, start_second, duration_seconds):
    # Converting everything to seconds:
    total_seconds_start = start_hour * 3600 + start_minute * 60 + start_second
    total_seconds_end = total_seconds_start + duration_seconds

    # Calculating hours, minutes, and seconds for the new time:
    new_hour = total_seconds_end // 3600
    new_minute = (total_seconds_end % 3600) // 60
    new_second = total_seconds_end % 60

    return new_hour, new_minute, new_second

# Getting user input:
start_hour = int(input("Enter the start hour: "))
start_minute = int(input("Enter the start minute: "))
start_second = int(input("Enter the start second: "))
duration_seconds = int(input("Enter the duration in seconds: "))

# Calculating the new time:
new_hour, new_minute, new_second = calculate_end_time(start_hour, start_minute, start_second, duration_seconds)

# Displaying the result:
print(f"The new end time is: {new_hour} hours, {new_minute} minutes, and {new_second} seconds.")

print(25*'-')

print("Exercise 50: ")

# Implemente um programa que calcule o ano de nascimento de uma pessoa
# a partir de sua idade e do ano atual.

age = int(input("Enter your age: "))
current_year = int(input("Enter the current year: "))

year_birthday = current_year - age

print(f"The year of your birth is: '{year_birthday}'.")


print(25*'-')

print("Exercise 50: ")

# Escreva um programa que leia as coordenadas x e y de pontos no R² e
# calcule sua distância da origem (0 0).

x = float(input("Enter the value for coordinate 'x': "))
y = float(input("Enter the value for coordinate 'y': "))

distance_until_origin = (x**2 + y**2)**(0.5)

print(f"The distance the given point until "
      f"origin is: '{distance_until_origin}.'")

print(f"The year of your birth is: '{distance_until_origin:.1f}'.")


print(25*'-')

print("Exercise 51: ")

# Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser
# repartido proporcionalmente ao valor que cada um deu para a realização
# da . Faça um programa que lera quanto cada apostador investiu,
# o valor do prêmio, e imprima quanto cada um ganharia do premio com
# base no valor investido.

value_bet1 = float(input("Amount bet by the first friend: R$ "))
value_bet2 = float(input("Amount bet by the second friend: R$ "))
value_bet3 = float(input("Amount bet by the third friend: R$ "))

value_prize = float(input("Enter the value for the prize: R$ "))

constant = (value_bet1 + value_bet2 + value_bet3) / value_prize

share_value1 = constant * value_bet1 * value_prize
share_value2 = constant * value_bet2 * value_prize
share_value3 = constant * value_bet3 * value_prize

print(f"The share of the first friend is: R$ {share_value1:.2f}")
print(f"The share of the second friend is: R$ {share_value2:.2f}")
print(f"The share of the third friend is: R$ {share_value3:.2f}")


print(25*'-')

"""

print("Exercise 52: ")

# Faça um programa para ler as dimensões de um terreno (comprimento
# 'c' e largura 'l'), bem como o preço do metro de tela 'p'. Imprima
# o custo para cercar este mesmo terreno com tela.


land_length = float(input("Enter a value for the length of land: "))
land_width = float(input("Enter a value for the width of land: "))
price_fence = float(input("Enter the price of the meter of fence: R$ "))

# Determining the the perimeter of the land:
perimeter = 2.0*(land_width+land_length)

total_price_fence = perimeter*price_fence

print(f"The total price to fence the land will be: "
	  f"R$ {total_price_fence: .2f}.")

print(25*'-')