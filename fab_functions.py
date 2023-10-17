# Task 1: Greeting Function
# Write a function `greet(name)` that takes a name as a parameter and prints a greeting message like "Hello, [name]!".

# The name parameter is for printing the users name
def greet_name(name):
    # Prints a greeting along with the name
    print("Hello " + name)
greet_name("Carlos")

# Task 2: Sum of Two Numbers
# Write a function `sum_numbers(a, b)` that takes two numbers as parameters and returns their sum.


def sum_numbers(a, b):
    # Takes two numbers and returns the sum of two
    print(a + b)
sum_numbers(38, 9)

# Task 3: Calculate Factorial
# Write a function `factorial(n)` that calculates the factorial of a given number `n`.

def factorial(n):
    factorial = 1 # makes it loop until 1
    for i in range(1, n + 1): 
        factorial = factorial * i
    print("The factorial of",n,"is",factorial)
factorial(5)

# Task 4: Check Even or Odd
# Write a function `is_even(num)` that takes a number as a parameter and returns `True` if the number is even, and `False` otherwise.

def is_even(num):
    if num % 2 == 0:
        print('True')
    else:
        print('False')
is_even(8)

# Task 5: Calculate Area of a Rectangle
# Write a function `calculate_area(length, width)` that calculates and returns the area of a rectangle given its length and width.

def calculate_area(length, width):
    n  = length * width
    print(n)
calculate_area(57, 20)