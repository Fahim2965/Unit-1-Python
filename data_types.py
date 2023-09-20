"""
TASK 1:
Create a float variable, and then convert it to an integer
Print both the original variable and the converted integer.

"""
# I created a float veriable and then converted it to an integer because that's what I was asked to do.

fl = 3.8
print(fl)
print(int(fl))


"""
TASK 2:
Write code that takes a number as input and prints whether 
it's positive, negative, or zero using if-elif-else statements.
"""
# First I asked the user for a number, then if the number is lover than 1 it's negative if it's higher than 1 it prints positive and if it does not match the requests it prints zero.


a = int(input("Number: "))
if a > 1:
    print("Positive")
elif a < 1:
    print("Negative")
else:
    print("Zero")


"""
TASK 3:

Write code that takes two numbers as input (an integer and a float), 
performs addition, subtraction, multiplication, and division, and prints the results.
"""

a = int(input("Give me an integer: "))
b = float(input("Give me a float: "))
add = a + b
sub = a - b
mul = a * b
div = a / b

print(add, sub, mul, div)


"""
TASK 4:

Create a dictionary with keys as fruit names and values as their respective quantities. 
Then print out the quantity of one of the fruits.
"""

fruits = {
    'apples': 10,
    'grapes': 8,
    }
print(fruits["grapes"])


"""
TASK 5:

Create a string variable with that is a list of numbers and convert that string into a tuple.
Then print out the both the original string and tuple.
"""

li = "1,2,3,4,6,5"
my_li = li.split(",")
print(tuple(my_li))