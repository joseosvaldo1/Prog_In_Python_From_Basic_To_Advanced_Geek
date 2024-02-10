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

"""

print("Exercise 38: ")
text_input_1 = "Enter an amount for the employee's salary: "
salary = float(input(text_input_1))

text_input_2 = "Enter a salary increase percentage: "
percentage_increase = float(input(text_input_2))

new_salary = (1 + percentage_increase/100)*salary

print(f"The new salary is: 'R$ {new_salary:.2f}'.")

print(25*'-')