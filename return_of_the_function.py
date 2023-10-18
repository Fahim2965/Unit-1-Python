"""
Task 1: Calculate the Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""

def a_num(a):
    return a ** 2
a_dumb = a_num(5)
print(a_dumb)
assert a_dumb == 25
try:
    assert a_num(5) == 7
except:
    print("The second assert is wrong!")

"""
Task 2: Calculate the Area of a Rectangle:
Write a function that takes the length and width of a rectangle and returns its area.
"""

def calculate_area(length, width):
    return length * width
der = calculate_area(57, 20)
print(der)
assert der == 1140
try:
    assert calculate_area(46, 27) == 21
except:
    print("The second assert is wrong!")

"""
Task 3: Convert Temperature from Celsius to Fahrenheit:
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""

def convert_c(c):
    return c * 9 / 5 + 32
F = convert_c(23)
print(F)
assert F == 73.4
try:
    assert convert_c(90) == 21
except:
    print("The second assert is wrong!")

"""
Task 4: Calculate the Average of Numbers:
Write a function that takes a list of numbers 
and returns the average (mean) of those numbers.
"""

def b_num(en):
    sam = sum(en)
    return sam/len(en)
print(b_num([37, 6, 8, 34]))
assert b_num([37, 6, 8, 34]) == 21.25

try:
    assert b_num([37, 6, 8, 34]) == 89
except AssertionError:
    print("Second assert is wrong!")