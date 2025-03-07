# Create a Python program that converts
# temperatures
# between
# Celsius
# and
# Fahrenheit. Prompt the user to enter a
# temperature value and the unit of
# measurement, and then display the
# converted temperature.
celsius = int(input("Enter temperature:-"))

fahrenheit = (celsius * 1.8) + 32

print('%.2f Celsius is equivalent to: %.2f Fahrenheit'% (celsius, fahrenheit))
