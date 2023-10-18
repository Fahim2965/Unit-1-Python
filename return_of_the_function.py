"""
Task 1: Calculate the Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""
#The return function does the process within the function
def a_num(a):
    return a ** 2
# Setting a variable to the function to print its result out of the function
a_dumb = a_num(5)
print(a_dumb)

# Setting assert to equal to value
assert a_dumb == 25

# The Try statement handles false assert gracefully
try:
    assert a_num(5) == 7
# To print out error and move on
except:
    print("The second assert is wrong!")

"""
Task 2: Calculate the Area of a Rectangle:
Write a function that takes the length and width of a rectangle and returns its area.
"""
# Creating a function for length and width
def calculate_area(length, width):
# Returns the values of length and width 
    return length * width
# Setting a variable to the function to print its result out of the function
der = calculate_area(57, 20)
print(der)

# Setting assert to equal to value
assert der == 1140

# The Try statement handles false assert gracefully
try:
    assert calculate_area(46, 27) == 21
# To print out error and move on
except:
    print("The second assert is wrong!")

"""
Task 3: Convert Temperature from Celsius to Fahrenheit:
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""

def convert_c(c):
# Making retun do Celcius to Fahrenheight formula 
    return c * 9 / 5 + 32
# converts 23C to Farenheight
F = convert_c(23)
print(F)

# Setting assert to equal to value
assert F == 73.4

# The Try statement handles false assert gracefully
try:
    assert convert_c(90) == 21
# To print out error and move on
except:
    print("The second assert is wrong!")

"""
Task 4: Calculate the Average of Numbers:
Write a function that takes a list of numbers 
and returns the average (mean) of those numbers.
"""

def b_num(en):
# Sets a variale to sum of parameter
    sam = sum(en)
# Returns the sum of all the numbers in the list  
    return sam/len(en)
# Variable takes the assigned sum and divides it by the amount of items
print(b_num([37, 6, 8, 34]))

# Setting assert to equal to value
assert b_num([37, 6, 8, 34]) == 21.25

# The Try statement handles false assert gracefully
try:
    assert b_num([37, 6, 8, 34]) == 89
# To print out error and move on
except AssertionError:
    print("Second assert is wrong!")