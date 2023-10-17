import datetime

"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""
# I imported date and the time from pydoc then used it to print the date and time of today
print(datetime.datetime.now())

"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""

# I used the datetime module and the strftime function to format the date and time to the U.S format
x = datetime.datetime.now()
print(x.strftime("%m/%d/%Y"))


"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""

# I two string variables to late convert them into dates
date1 = "09 06 2023"
date2 = "10 20 2023"

# Adds 2 variables of strings to dates
datee1 = datetime.datetime.strptime(date1, "%m %d %Y")
datee2 = datetime.datetime.strptime(date2, "%m %d %Y")

# Uses strptime to format the variables into a date, as month / day / year
difference = (datee2 - datee1).days

# Findes the difference of date and time
print("The difference is", difference, "days")

"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""

bday = input("What is your birthday, MM/DD/YYYY: ")