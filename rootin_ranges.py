"""
Exercise 1:
Write a program to print numbers from 1 to 10 using a for loop.
"""
# I set a range from 1 to 11 because computers count from 0 so thats why I set it from 1 to 11
for x in range(1, 11):
    print(x)
print("-------------->")

"""
Exercise 2:
Write a program to count by 10s from 900 to 1000
"""
# The for loop will range from 900 to 1000 and count from 900 to 1000 in increments of 10
for x in range(900, 1001, 10):
    print(x)
print("--------------->")

"""
Exercise 3:
Write a program that counts form 1-100 by 9
"""
# The for loop will range from 1 to 100 and count in increments of 9
for x in range(1, 101, 9):
    print(x)
print("--------------->")

"""
Exercise 4:
Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.
"""
# Empty variable for the total
sum = 0
for x in range(1, 11):
    sum += x # Will calculate the sum of all numbers from 1 to 10
    print(sum) # prints the sum of the each number
print("--------------->")

"""
Excercise 5:
Uncomment the following code and run it. Then answer the following:
- What is the ouput of the code?

- Explain the iterative process that this code executes to get that output
"""
# the output is * in 5 rows and with each iteration it adds one more
# Through each iteration it adds one more to i which is created in the first loop
# Then prints the * in increments of 1 through each ineration
rows = 5
 
for i in range(rows):
     for j in range(i + 1):
         print('*', end=' ')
     print()