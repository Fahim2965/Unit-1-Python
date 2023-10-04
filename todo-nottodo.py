todos = []    # This empty list holds the users todos
todos.append(input("What would you like to add to your todo list: ")) # This allows the user to add the tasks
while True:  # The while loop is to continuously run the loop
    print("")
    print(todos) # This is to print the todos
    print("")
    b = input("Do you want to add new tasks? Yes/No ") # This askes the user if they want add new todos
    if b == "Yes" or b == "yes": 
        todos.append(input("Add new task: ")) # This adds the new tods to the list
    elif b == "No" or b == "no":
        c = input("Do you want to remove a task? Yes/No ")
        if c == "Yes" or c == "yes":
            todos.remove(input("Which task would you like to remove: ")) # Thsi removes any tasks the user would like to remove
        else:
            continue # If theuseer does not chose anything the code will continue to run
