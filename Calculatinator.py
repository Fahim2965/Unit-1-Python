print("Welcome to my Calculatinator-inator 9000")
print()


a = float(input("First number: ")) # This askes the use for a number

print()

b = float(input("Secons number: ")) # Does the same as a

print()

print('''
Select operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Floor Division
6. Exponential
7. Remainder
''')
      
c = int(input("Enter choice: ")) # This takes the users choice and runs the following


# The if and the elif statements run all the operations and gives the user the out put

if c == 1:
    d = a + b
    print(d)
elif c == 2:
    d = a - b
    print(d)
elif c == 3:
    d = a * b
    print(d)
elif c == 4:
    d = a / b
    print(d)
elif c == 5:
    d = a // b
    print(d)
elif c == 6:
    d = a ** b
    print(d)
elif c == 7:
    d = a % b
    print(d)
else:                     # The else statement is there if any of the conditions are not met
    print("Select a number from the list in order to calculate.")

