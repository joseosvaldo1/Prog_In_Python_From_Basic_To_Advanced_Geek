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

"""

print("Exercise 7: ")
question = "Enter the temperature in Farenheit: "
temperature_in_farenheit= float(input(question))
temperature_in_celsius = (5.0*(temperature_in_farenheit - 32.0))/9.0

print(f"The temperature in Farenheit is: " 
      f"'{temperature_in_celsius} ºC'")

print(25*'-')
