# The try statement tyes the code and the excepts.
try:
    age = int(input('Enter your age: '))

    faveNum = int(input('What is your favorite number: '))

    if age <= 21:
        print('You are not allowed to enter, you are too young.')
    else:
        print('Welcome, you are old enough.')

        print("Fun Fact! Your age divided by your favorite number is: " , age / faveNum)

# This except is for the zerodivision error and if that were to occure it would run the print statement in the except statement.
except ZeroDivisionError:
    print("Please enter a favorite number other than 0 because you are unable to devide by 0")

# The same will occure at this except if the conditions are meet the print statement withen the except statement will will run.
except ValueError:
    print("Please enter a integer like 10 and not ten")