'''
TASK 1 Even or Odd
Determine if a number is even or odd.
'''

number = int(input("Please enter a number: "))
number = number % 2

if number == 0:
    print("This is a even number.")
else:
    print("This is a odd number.")


'''
TASK 2 Positive, Negative, or Zero:
Determine if a number is positive, negative, or zero.

EXTRA CREDIT: Tell the user if they did not enter a valid number
'''

a = float(input("Enter a number: "))
if a <= -1:
    print("It's a negative number.")
elif a == 0:
    print("It's a zero.")
else:
    print("It's positive")

'''
TASK 3: Largest of Three
Find and print the largest of three numbers.
'''

c = [1,2,3]
b = max(c)
print(b)



'''
TASK 4: Leap Year
Determine if a year is a leap year or not.
'''

year = int(input("Please enter a year: "))
if year % 4 == 0:
    print("This is a leap year.")
else:
    print("Sorry this is not a leap year")


'''
TASK 5: Vowel or Consonant:
Identify if a character is a vowel or consonant.

EXTRA CREDIT: Tell the user if they did not enter a valid letter
'''


try:
    ips = str(input("Enter a character: "))
except ValueError:
    print()