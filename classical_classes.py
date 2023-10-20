"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""

# Created a class with the name Person
class Person():
    
    # init method for the name and age
    def __init__(self, name, age):
     self.name = name
     self.age = age

     # Prints the name and age
    def hi(self):
       print(self.name)
       print(self.age)

# Assigns class to a variable 
Fahim = Person(str("Fahim"), 16)

# Prints the hi method
Fahim.hi()
    
"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""

# Initial class for the template
class Animal():
   # Method called speak to print what they say
   def speak(self):
    print()

# Dog class using the animal template
class Dog():
  # Method called speak to print what they say
  def speak(self):
    print("Bark")

# Calls the variables to print the speak method
speak = Dog()
speak.speak()

# Cat class using the animal template
class Cat():
  def speak(self):
    print("Meow")

# Calls the variables to print the speak method
speak = Cat()
speak.speak()


"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""

# Creating class for bank account
class BankAccount():
    # innit method for all starter 
    def __init__(self, balance, owner): 
        self.balance = balance
        self.owner = owner
    
    # Method for printing total balance in the bank
    def total(self): 
        print('Your balance is ' + str(self.balance))

     # Method for adding deposit and printing total value
    def deposit(self, depo):
        self.balance = self.balance + depo
        print('Your total balance is ' + str(self.balance))

    # Method for substracting and withdraw then printing the total value
    def withdraw(self, withd):
        self.balance = self.balance - withd
        print('Your total balance is ' + str(self.balance))

# Assigning class to variable
t3_bank = BankAccount(500, 'a')
# Prints the total in balance
t3_bank.total() 
# Deposit method for adding and printing balance
t3_bank.deposit(200)
# Withdraw method for substracting and printing balance
t3_bank.withdraw(100)