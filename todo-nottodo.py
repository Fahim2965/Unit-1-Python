#Creats an empty variables for a list 
Todo = []
Choices = ''

#Sets the continuation and stopping variables for the while loop
while Choices != 'Stop':
    print()
    print('Your todos are:')
    print(Todo)
    print()
#This gives the user choices to add, delete, or check the list.
    Choices = input('Please select an option. "Add" : 1, "Delete" : 2 or "Stop" : 3 to stop:  ')
    print()
    if Choices == "Add" or Choices == "1" :
#Asks user what they want to add to list
        Addtodo = input('What would you like to add to your list: ')
        Todo.append(Addtodo)
        print()
        print(Addtodo + ' was added!')
        print()
    
#elif activates based on conditional (del varient)
    elif Choices == "Delete" or Choices == "2" :
        Deltodo = int(input("Please select the number for the item in the list you'd like to remove: "))
#deletes specified item with -1 to make it user friendly on indexes
        del Todo[Deltodo - 1]
        print("Your selected statement has been deleted!")
        print()

#Stops loop if conditionals are met
    elif Choices == "Stop" or Choices == "3" :
        print('Statement is now stopping')
        print()
        break

#Repeats the loop if no conditionals are met
    else :
        print('The answer chosen is invalid.')
        print()