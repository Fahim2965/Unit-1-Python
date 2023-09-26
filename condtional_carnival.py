'''
TASK 1 Even or Odd
Determine if a number is even or odd.
'''
#first i asked for input and then got the remainder to see if its even or not

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

# first i asked for input and then i checked using if else for negative and positive

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
#first i made a list and then got the max using the max statement and then printed it in a variable 

c = [1,2,3]
b = max(c)
print(b)



'''
TASK 4: Leap Year
Determine if a year is a leap year or not.
'''
#first i got the year by using the input and then i used % to get the remainder by 4 and then get if its a leap year

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