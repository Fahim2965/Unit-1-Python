"""
Exercise 1:
Write a program to print each character of a given string using a for loop.
"""
# First I made a variable than made a for loop to print each character in the string

A = "Xavier20"
for x in A:
    print(x)

"""
Exercise 2:
Write a program to calculate the sum of elements in a list using a for loop.
"""
# I created a list then used the sum element to calculate the sum of the numbers in the list

a = [2, 4]
sum = 0
for f in a:
    sum += f
    print(sum)
    print("------------------------>")

"""
Exercise 3:
Write a program to print the length of each word in a sentence using a for loop and a list.
"""
# I first created a strying then converted it into a list and then printed 

B = 'Aftab is home'
B = B.split(" ")
for w in B:
    print(w)
    print(len(w))
    print("------------------------>")


"""
Excercise 4:
Write a program that creates a dictionary (atleast 4 key:value pairs) and then
iterates through a dictionary and prints the result

In a comment, answer the following, what do you notice about the output of your code?
Is it what you expected?
""" # Only the Keys print out and none of the values print

b =  {
    "Pan": 1.50,
    "Manzanas": 2.50,
    "Agua": 3.50
}

for tr in b:
    print(tr)
