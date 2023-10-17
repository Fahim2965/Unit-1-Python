"""
Task 1: Calculate the Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""

def a_num(a):
    return a ** 2
a_dumb = a_num(5)
print(a_dumb)

"""
Task 2: Calculate the Area of a Rectangle:
Write a function that takes the length and width of a rectangle and returns its area.
"""

def calculate_area(length, width):
    return length * width
der = calculate_area(57, 20)
print(der)

"""
Task 3: Convert Temperature from Celsius to Fahrenheit:
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""

def convert_c(c):
    return c * 9 / 5 + 32
F = convert_c(23)
print(F)


"""
Task 4: Calculate the Average of Numbers:
Write a function that takes a list of numbers 
and returns the average (mean) of those numbers.
"""

