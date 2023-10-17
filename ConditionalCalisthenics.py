'''
Exercise 1:
Check if an integer is even and greater than 10.
Return True if both conditions are met, False otherwise.
'''
# First i made a variable and then i made a >= to ten in order to give an true or false result
a = '10'
if int(a) >= 10:
    print('True')
else:
    print('False')


'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''

# First I asked the user for their age and then their education and I used an if statement with an or in order to check for both 
# I made an else to make sure if both are false they would pay 20
b = int(input('What is your age: '))
c = input('Education?: ')
if b < 18 or c == 'yes':
    print("Price is $10")
else:
    print('Price is $20')


'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''

# First i made a list with 3 fruits then after i made an input and a if statement checking if they got it right
fruits = ['apples', 'oranges', 'watermelon']
ak = input('Give me a fruit name: ')
if ak in fruits:
    print('Yes, that fruit is in the list.')
else:
    print("No, that fruit is not in the list.")


'''
Exercise 4:
Check if a year is a century year and a leap year.
'''

# First i asked for a year input and the used if elif and else to check for both leap and century year and then for the rest if both
tr = int(input('Enter year: '))
if tr % 4 == 0:
    print('The year is a leap year')
elif tr % 100 == 0:
    print('The year is a century year')
else:
    print('The year is neither century or leap')

'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''

# First I asked for two inputs for zone and weight and then I did an if statement comparing the zone input first and then multiplying
w = input('Please input package weigth: ')
z = input('Please input zone (A or B): ')
if z == 'A':
    p = float(w) * 5
    print('The price for zone A would be ' + p)
elif z == 'B':
    p = float(w) * 7
    print('The price for zone B would be ' + p)
else:
    print('Please put a valid zone')


'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''

